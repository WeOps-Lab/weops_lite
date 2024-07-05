export default class CachedPromise {
    cache: {};
    constructor() {
        this.cache = {}
    }

    /**
     *根据 id 获取请求对象，如果不传入 id，则获取整个队列
     *
     * @param {string?} id id
     *
     * @return {Array|Promise}
     */
    get(id) {
        if (typeof id === 'undefined') {
            return Object.keys(this.cache).map(requestId => this.cache[requestId])
        }
        return this.cache[id]
    }

    /**
     *设置新的请求对象到请求队列中
     *
     * @param {string} id id
     * @param {Promise} promise
     *
     * @return {Promise} promise
     */
    set(id, promise) {
        this.cache = Object.assign({}, this.cache, { [id]: promise })
    }

    /**
     * 根据 id 删除请求对象
     *
     * @param {string|Array?} deleteIds 要 删除 的请求 id，如果不传，则 删除 所有请求
     *
     * @return {Promise} Promise
     */
    delete(deleteIds) {
        let requestIds = []
        if (typeof deleteIds === 'undefined') {
            requestIds = Object.keys(this.cache)
        } else if (deleteIds instanceof Array) {
            deleteIds.forEach(id => {
                if (this.get(id)) {
                    requestIds.push(id)
                }
            })
        } else if (this.get(deleteIds)) {
            requestIds.push(deleteIds)
        }

        requestIds.forEach(requestId => {
            delete this.cache[requestId]
        })

        return Promise.resolve(deleteIds)
    }
}
