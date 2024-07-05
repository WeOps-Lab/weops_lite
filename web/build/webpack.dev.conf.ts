// @ts-ignore
'use strict'
const utils = require('./utils.ts')
const webpack = require('webpack')
const config = require('../config/index.ts')
const {merge} = require('webpack-merge')
const path = require('path')
const baseWebpackConfig = require('./webpack.base.conf.ts')
const HtmlWebpackPlugin = require('html-webpack-plugin')
const portfinder = require('portfinder')

const HOST = process.env.HOST
const PORT = process.env.PORT && Number(process.env.PORT)

const devWebpackConfig = merge(baseWebpackConfig, {
    mode: 'development',
    module: {
        rules: utils.styleLoaders({sourceMap: config.dev.cssSourceMap, usePostCSS: true})
    },
    // cheap-module-eval-source-map is faster for development
    // devtool: config.dev.devtool,

    // these devServer options should be customized in /config/index.ts
    devServer: {
        client: {
            logging: 'warn',
            overlay: config.dev.errorOverlay
            ? {warnings: false, errors: true}
            : false,
        },
        static: {
            publicPath: config.dev.assetsPublicPath,
        },
        historyApiFallback: {
            rewrites: [
                {
                    from: /.*/,
                    to: path.posix.join(
                        config.dev.assetsPublicPath,
                        "index-dev.html"
                    ),
                },
            ],
        },
        compress: true,
        host: HOST || config.dev.host,
        port: PORT || config.dev.port,
        open: config.dev.autoOpenBrowser,
        proxy: config.dev.proxyTable,
    },
    plugins: [

        new webpack.HotModuleReplacementPlugin(),

        // https://github.com/ampedandwired/html-webpack-plugin
        new HtmlWebpackPlugin({
            filename: 'index-dev.html',
            template: 'index-dev.html',
            inject: true,
            chunks: ['app']
        }),
        new webpack.ProvidePlugin({
            $: 'jquery',
            jQuery: 'jquery',
            jquery: 'jquery',
            'window.jQuery': 'jquery'
        }),
        new webpack.DefinePlugin({
            'process.env.USE_MOCK': JSON.stringify(process.env.USE_MOCK)
        })
    ],
    optimization: {
        noEmitOnErrors: true
    }
})

module.exports = new Promise((resolve, reject) => {
    portfinder.basePort = process.env.PORT || config.dev.port
    portfinder.getPort((err, port) => {
        if (err) {
            reject(err)
        } else {
            // publish the new Port, necessary for e2e tests
            process.env.PORT = port
            // add port to devServer config
            devWebpackConfig.devServer.port = port

            resolve(devWebpackConfig)
        }
    })
})
