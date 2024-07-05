import axios from 'axios'
// import bus from '../../common/bus'
import CachedPromise from './cached-promise'
import RequestQueue from './request-queue'
import Vue from 'vue'

const vm = new Vue()

const getToken = () => {
    const DEFAULT_X_CSRFTOKEN = 'NOTPROVIDED'
    const { cookie } = document
    if (cookie && typeof cookie === 'string') {
        const key = window['CSRF_COOKIE_NAME'] || 'csrftoken'
        const patten = new RegExp(`^${key}=[\S]*`, 'g')
        const values = cookie.split(';')
        const value = values.find((item) => patten.test(item.trim()))
        if (!value) return DEFAULT_X_CSRFTOKEN
        return decodeURIComponent(value.split('=')[1] || DEFAULT_X_CSRFTOKEN)
    }
    return DEFAULT_X_CSRFTOKEN
}

// axios 实例
const axiosInstance = axios.create({
    xsrfCookieName: 'backend_csrftoken',
    xsrfHeaderName: 'X-CSRFToken',
    withCredentials: true,
    baseURL: window['siteUrl']
})

/**
 * request interceptor
 */
axiosInstance.interceptors.request.use(config => {
    const token = vm.$keycloak?.token || getToken()
    config.headers['AUTHORIZATION'] = token
    config.headers['X-Requested-With'] = 'XMLHttpRequest'
    return config
})

// 响应拦截

const http = {
    queue: new RequestQueue(),
    cache: new CachedPromise(),
    cancelRequest: requestId => {
        return http.queue.cancel(requestId)
    },
    cancelCache: requestId => http.cache.delete(requestId),
    cancel: (requestId) => {
        Promise.all([http.cancelRequest(requestId), http.cancelCache(requestId)])
    }
}

const methodsWithoutData = ['get', 'head', 'options']
const methodsWithData = ['delete', 'post', 'put', 'patch']
const allMethods = [...methodsWithoutData, ...methodsWithData]

// 在自定义对象 http 上添加各请求方法
allMethods.forEach(method => {
    Object.defineProperty(http, method, {
        get() {
            return getRequest(method)
        }
    })
})

/**
 * 获取 http 不同请求方式对应的函数
 *
 * @param {string} http method 与 axios 实例中的 method 保持一致
 *
 * @return {Function} 实际调用的请求函数
 */
function getRequest(method) {
    return (url, data, config) => {
        return getPromise(method, url, data, config)
    }
}

/**
 * 实际发起 http 请求的函数，根据配置调用缓存的 promise 或者发起新的请求
 *
 * @param {string} method http method 与 axios 实例中的 method 保持一致
 * @param {string} url 请求地址
 * @param {Object} data 需要传递的数据, 仅 post/put/patch 三种请求方式可用
 * @param {Object} userConfig 用户配置，包含 axios 的配置与本系统自定义配置
 *
 * @return {Promise} 本次http请求的Promise
 */
async function getPromise(method, url, data, userConfig = {}) {
    const config = initConfig(method, url, userConfig)
    let promise
    if (config.cancelPrevious) {
        await http.cancel(config.requestId)
    }

    if (config.clearCache) {
        http.cache.delete(config.requestId)
    } else {
        promise = http.cache.get(config.requestId)
    }

    if (config.fromCache && promise) {
        return promise
    }

    promise = new Promise(async(resolve, reject) => {
        const axiosRequest = methodsWithData.includes(method)
            ? axiosInstance[method](url, data, config)
            : axiosInstance[method](url, config)

        try {
            const response = await axiosRequest
            Object.assign(config, response.config || {})
            handleResponse({ config, response, resolve, reject })
        } catch (httpError) {
            // http status 错误
            // 避免 cancel request 时出现 error message
            if (httpError && httpError.message && httpError.message.type === 'cancel') {
                console.warn('请求被取消：', url)
                return
            }

            Object.assign(config, httpError.config)
            reject(httpError)
        }
    }).catch(codeError => {
        // code 错误
        return handleReject(codeError, config)
    }).finally(() => {
        http.queue.delete(config.requestId)
    })

    // 添加请求队列
    http.queue.set(config)
    // 添加请求缓存
    http.cache.set(config.requestId, promise)

    return promise
}

/**
 * 处理 http 请求成功结果
 *
 * @param {Object} 请求配置
 * @param {Object} cgi 原始返回数据
 * @param {Function} promise 完成函数
 * @param {Function} promise 拒绝函数
 */
function handleResponse({ config, response, resolve, reject }) {
    // 容器服务 -> 配置 -> heml 模板集 helm/getQuestionsMD 请求 response 是一个 string 类型 markdown 文档内容
    if (typeof response === 'string') {
        resolve(response, config)
        return
    }

    if (response.data && response.data.code !== 0 && config.globalError) {
        reject({ response })
        return
    }

    if (config.originalResponse) {
        resolve(response)
        return
    }

    resolve(response.data)
}

// 不弹tips的特殊状态码
const CUSTOM_HANDLE_CODE = [4005, 4003, 4005002, 4005003, 4005005]
/**
 * 处理 http 请求失败结果
 *
 * @param {Object} Error 对象
 * @param {config} 请求配置
 *
 * @return {Promise} promise 对象
 */
function handleReject(error, config) {
    if (axios.isCancel(error) || (error && error.message === 'Request aborted')) {
        return Promise.reject(error)
    }
    if (error.response) {
        const { status, data } = error.response
        let message = (error && error.message) || (data && data.message)
        if (status === 401) {
            message = '未登录'
            vm.$error(message)
            vm.$keycloak.logoutFn()
        } else if (status === 500) {
            message = '系统出现异常'
        } else if (status === 403) {
            message = '无权限操作'
        } else if ([4005, 4003].includes((data && data.code))) {
            // bus.$emit('show-apply-perm-modal', data?.data)
        }
        if ((data && data.code) === 500 && (data && data.request_id)) { // code为500的请求需要带上request_id
            message = `${message}( ${(data && data.request_id.slice(0, 8))} )`
        }

        if (config.globalError && !CUSTOM_HANDLE_CODE.includes((data && data.code))) {
            message && console.log(message)
        }
    } else if (error.message === 'Network Error') {
        // console.log('网络错误')
    } else if (error.message && config.globalError) {
        // console.log(error.message)
    }
    return Promise.reject(error)
}

/**
 * 初始化本系统 http 请求的各项配置
 *
 * @param {string} http method 与 axios 实例中的 method 保持一致
 * @param {string} 请求地址, 结合 method 生成 requestId
 * @param {Object} 用户配置，包含 axios 的配置与本系统自定义配置
 *
 * @return {Promise} 本次 http 请求的 Promise
 */
function initConfig(method, url, userConfig) {
    const defaultConfig = {
        ...getCancelToken(),
        // http 请求默认 id
        requestId: method + '_' + url,
        // 是否全局捕获异常
        globalError: true,
        // 是否直接复用缓存的请求
        fromCache: false,
        // 是否在请求发起前清楚缓存
        clearCache: false,
        // 响应结果是否返回原始数据
        originalResponse: false,
        // 当路由变更时取消请求
        cancelWhenRouteChange: true,
        // 取消上次请求
        cancelPrevious: false
    }
    return Object.assign(defaultConfig, userConfig)
}

/**
 * 生成 http 请求的 cancelToken，用于取消尚未完成的请求
 *
 * @return {Object} {cancelToken: axios 实例使用的 cancelToken, cancelExcutor: 取消http请求的可执行函数}
 */
function getCancelToken() {
    let cancelExcutor
    const cancelToken = new axios.CancelToken(excutor => {
        cancelExcutor = excutor
    })
    return {
        cancelToken,
        cancelExcutor
    }
}

export default http
