// @ts-ignore
'use strict'
const path = require('path')
const config = require('../config/index.ts')
const packageConfig = require('../package.json')
const MiniCssExtractPlugin = require('mini-css-extract-plugin')
const DllReferencePlugin = require('webpack/lib/DllReferencePlugin')

exports.assetsPath = function (_path) {
    const assetsSubDirectory = process.env.NODE_ENV === 'production'
        ? config.build.assetsSubDirectory
        : config.dev.assetsSubDirectory

    return path.posix.join(assetsSubDirectory, _path)
}

exports.cssLoaders = function (options) {
    options = options || {}

    const cssLoader = {
        loader: 'css-loader',
        options: {
            sourceMap: options.sourceMap
        }
    }

    const postcssLoader = {
        loader: 'postcss-loader',
        options: {
            sourceMap: options.sourceMap
        }
    }

    // generate loader string to be used with extract text plugin
    function generateLoaders(loader, loaderOptions) {
        const loaders = options.usePostCSS ? [cssLoader, postcssLoader] : [cssLoader]

        if (loader) {
            loaders.push({
                loader: loader + '-loader',
                options: Object.assign({}, loaderOptions, {
                    sourceMap: options.sourceMap
                })
            })
        }

        // Extract CSS when that option is specified
        // (which is the case during production build)
        if (process.env.NODE_ENV === 'production') {
            const extractLoader = {
                loader: MiniCssExtractPlugin.loader,
                options: {
                    publicPath: '../../../../'
                }
            }
            // @ts-ignore
            return [extractLoader].concat(loaders)
        } else {
            // @ts-ignore
            return ['vue-style-loader'].concat(loaders)
        }
    }

    // https://vue-loader.vuejs.org/en/configurations/extract-css.html
    return {
        // @ts-ignore
        css: generateLoaders(),
        // @ts-ignore
        postcss: generateLoaders(),
        // @ts-ignore
        less: generateLoaders('less'),
        sass: generateLoaders('sass', {indentedSyntax: true}),
        // @ts-ignore
        scss: generateLoaders('sass').concat(
            {
                loader: 'sass-resources-loader',
                options: {
                    resources: path.resolve(__dirname, '../src/assets/base/css/color.scss') //这里是单独建的存放变量的scss，我的是 var.scss
                }
            }),
        // @ts-ignore
        stylus: generateLoaders('stylus'),
        // @ts-ignore
        styl: generateLoaders('stylus')
    }
}

// Generate loaders for standalone style files (outside of .vue)
exports.styleLoaders = function (options) {
    const output = []
    const loaders = exports.cssLoaders(options)

    for (const extension in loaders) {
        const loader = loaders[extension]
        output.push({
            test: new RegExp('\\.' + extension + '$'),
            use: loader
        })
    }

    return output
}

exports.createNotifierCallback = () => {
    const notifier = require('node-notifier')

    return (severity, errors) => {
        if (severity !== 'error') return

        const error = errors[0]
        const filename = error.file && error.file.split('!').pop()

        notifier.notify({
            title: packageConfig.name,
            message: severity + ': ' + error.name,
            subtitle: filename || '',
            icon: path.join(__dirname, 'logo.png')
        })
    }
}


exports.getDllManifest = () => {
    let plugins = []
    Object.keys({
        vendors: ['vue/dist/vue.esm.js', 'vuex', 'vue-router', 'axios'],
        jquery: ['jquery'],
        echarts: ['echarts'],
        antv: ['@antv/g2']
    }).forEach((name) => {
        plugins.push(
            new DllReferencePlugin({
                context: path.resolve(__dirname, config.build.assetsRoot, 'static'),
                manifest: require(path.resolve(__dirname, config.build.assetsRoot, 'static/dist/dll/[name].manifest.json').replace(/\[name\]/gi, name))
            })
        )
    })
    return plugins
}
