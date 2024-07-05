import httpConfig from './request'

const methodsWithoutData = ['get', 'head', 'options', 'delete']
const defaultConfig = { needRes: true }

const json2Query = (param, key) => {
    const mappingOperator = '='
    const separator = '&'
    let paramStr = ''

    if (param instanceof String || typeof param === 'string' || param instanceof Number ||
        typeof param === 'number' || param instanceof Boolean || typeof param === 'boolean'
    ) {
        // @ts-ignore
        paramStr += separator + key + mappingOperator + encodeURIComponent(param)
    } else if (typeof param === 'object') {
        if (key) {
            paramStr += separator + key + mappingOperator + JSON.stringify(param)
        } else {
            Object.keys(param).forEach(p => {
                if (param[p] !== undefined) {
                    const value = param[p]
                    const k = (key === null || key === '' || key === undefined)
                        ? p
                        : key + (param instanceof Array ? '[' + p + ']' : '.' + p)
                    paramStr += separator + json2Query(value, k)
                }
            })
        }
    }
    return paramStr.substr(1)
}

export const request = (method, url) => (params = {}, config = {}) => {
    const reqMethod = method.toLowerCase()
    const reqConfig = Object.assign({}, defaultConfig, config)

    // 全局URL变量替换
    const variableData = {}

    Object.keys(params).forEach(key => {
        // 自定义url变量
        if (key.indexOf('$') === 0) {
            variableData[key] = params[key]
        }
    })

    let newUrl = `${url}`
    Object.keys(variableData).forEach(key => {
        if (!variableData[key]) {
            // 去除后面的路径符号
            newUrl = newUrl.replace(new RegExp(`\\${key}/`, 'g'), '')
        } else {
            newUrl = newUrl.replace(new RegExp(`\\${key}`, 'g'), variableData[key])
        }
        delete params[key]
    })

    let req = null
    if (methodsWithoutData.includes(reqMethod)) {
        // 拼接参数
        const query = json2Query(params, '')
        if (query) {
            newUrl += `?${query}`
        }
        req = httpConfig[reqMethod](newUrl, null, reqConfig)
    } else if (reqMethod === 'deleteb') {
        req = httpConfig['delete'](newUrl, { data: params, ...reqConfig })
    } else {
        req = httpConfig[reqMethod](newUrl, params, reqConfig)
    }
    return req.then((res) => {
        if (reqConfig.needRes) return Promise.resolve(res)

        return Promise.resolve(res.data)
    }).catch((err) => {
        return Promise.reject(err)
    })
}

const getPromise = (method, url, params, config = {}) => {
    return new Promise(async(resolve, reject) => {
        await request(method, url)(params, config).catch(e => e.response.data)
            .then(res => resolve(res))
            .catch(err => reject(err))
    })
}

// get
export const get = (url, params, opts = {}) =>
    getPromise('get', url, params, opts)

// post
export const post = (url, params, opts = {}) =>
    getPromise('post', url, params, opts)

// put
export const put = (url, params, opts = {}) =>
    getPromise('put', url, params, opts)

// delete
export const deletes = (url, params, opts = {}) =>
    getPromise('delete', url, params, opts)

// deleteb body传参
export const deleteb = (url, params, opts = {}) =>
    getPromise('deleteb', url, params, opts)

// patch
export const patch = (url, params, opts = {}) =>
    getPromise('patch', url, params, opts)

export const reUrl = process.env.USE_MOCK ? 'http://yapi.canway.top/mock/3436/api' : '/api'
