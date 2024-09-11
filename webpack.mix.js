let mix = require('laravel-mix');

const webpack = require('webpack')

const dotenvplugin = new webpack.DefinePlugin({
    'process.env': {
        BASE_URL: JSON.stringify(process.env.BASE_URL || ''),
    },
})

mix.webpackConfig({
    stats: {
        children: true,
    },
    plugins: [dotenvplugin],
})

mix.sass('website/assets/scss/app.scss', 'website/static/website/css/app.css').sourceMaps().options({ processCssUrls: false });
mix.js('website/assets/js/app.js', 'website/static/website/js/app.js').sourceMaps();