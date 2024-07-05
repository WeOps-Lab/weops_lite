// @ts-ignore
'use strict'
const utils = require('./utils.ts')
const config = require('../config/index.ts')
const {merge} = require('webpack-merge')
const baseWebpackConfig = require('./webpack.base.conf.ts')
const HtmlWebpackPlugin = require('html-webpack-plugin')
const CssMinimizerPlugin = require("css-minimizer-webpack-plugin");
const MiniCssExtractPlugin = require('mini-css-extract-plugin')
const TerserPlugin = require('terser-webpack-plugin')
const ReplaceTemplateStaticUrlPlugin = require('./replace-template-static-url-plugin.ts')
const date = new Date()
const time = `${date.getFullYear()}${date.getMonth() + 1 < 10 ? `0${date.getMonth() + 1}` : date.getMonth() + 1}${date.getDate() < 10 ? `0${date.getDate()}` : date.getDate()}`
const webpackConfig = merge(baseWebpackConfig, {
    mode: 'production',
    output: {
        publicPath: './',
        path: config.build.assetsRoot,
        filename: utils.assetsPath('js/[name].[chunkhash].js'),
        chunkFilename: utils.assetsPath('js/[name].[chunkhash].js')
    },
    // devtool: config.build.productionSourceMap ? config.build.devtool : false,
    optimization: {
        // 压缩
        minimize: true,

        minimizer: [
            new CssMinimizerPlugin(),
            new TerserPlugin({
                terserOptions: {
                    mangle: true,
                    compress: {
                        drop_debugger: false
                    }
                },
                parallel: true, // 多进程并发运行
                extractComments: false, // 不将注释剥离到单独的文件
                cache: true // 缓存

            })
        ],

        runtimeChunk: {
            name: 'manifest'
        },
    },
    module: {
        rules: utils.styleLoaders({
            sourceMap: config.build.productionSourceMap,
            extract: true,
            usePostCSS: true
        })
    },
    plugins: [
        ...utils.getDllManifest(),

        new MiniCssExtractPlugin({
            filename: utils.assetsPath('css/[name].[chunkhash].css'),
            chunkFilename: utils.assetsPath('css/[name].[chunkhash].css'),
            ignoreOrder: true
        }),

        // generate dist index.html with correct asset hash for caching.
        // you can customize output by editing /index.html
        // see https://github.com/ampedandwired/html-webpack-plugin
        new HtmlWebpackPlugin({
            filename: config.build.index,
            template: 'index.html',
            inject: true,
            minify: {
                removeComments: true,
                collapseWhitespace: true,
                removeAttributeQuotes: true
                // more options:
                // https://github.com/kangax/html-minifier#options-quick-reference
            },
            sourceMap: true,
            staticUrl: '{{ STATIC_URL }}',
            timeStamp: time
        }),
        new ReplaceTemplateStaticUrlPlugin()
    ]
})

if (config.build.productionGzip) {
    const CompressionWebpackPlugin = require('compression-webpack-plugin')

    webpackConfig.plugins.push(
        new CompressionWebpackPlugin({
            asset: '[path].gz[query]',
            algorithm: 'gzip',
            test: new RegExp(
                '\\.(' +
                config.build.productionGzipExtensions.join('|') +
                ')$'
            ),
            threshold: 10240,
            minRatio: 0.8
        })
    )
}

if (config.build.bundleAnalyzerReport) {
    const BundleAnalyzerPlugin = require('webpack-bundle-analyzer').BundleAnalyzerPlugin
    webpackConfig.plugins.push(new BundleAnalyzerPlugin())
}

module.exports = webpackConfig
