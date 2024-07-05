/* eslint-disable */
(function(global, factory) {
    typeof exports === 'object' && typeof module !== 'undefined'
        ? module.exports = factory()
        : typeof define === 'function' && define.amd
            ? define(factory)
            : (global = global || self, global.microRouter = factory())
}(this, function() {
    'use strict'
    // 微前端路由合并
    const files = require.context('@/projects', true, /frameRouter.ts/)
    let frameRouter = []
    let adminRouteConfig = []

    files.keys().forEach(key => {
        frameRouter = frameRouter.concat(files(key).frameRouter).filter(item => !!item)
        adminRouteConfig = adminRouteConfig.concat(files(key).adminRouteConfig).filter(item => !!item)
    })
    return {
        frameRouter,
        adminRouteConfig
    }
}))
