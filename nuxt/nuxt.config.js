import colors from 'vuetify/es5/util/colors'
// const axios = require("axios");
// require('dotenv').config();
// const { HOST_URL } = process.env;

export default {
  publicRuntimeConfig: {
    // baseURL: process.env.BASE_URL || 'https://nuxtjs.org'
    // HOST_URL: process.env.HOST_URL || 'http://localhost:3001'
    HOST_URL: process.env.HOST_URL || 'http://flask:5000'
  },
  privateRuntimeConfig: {
    // baseURL: process.env.BASE_URL || 'https://nuxtjs.org'
    // HOST_URL: process.env.HOST_URL || 'http://localhost:3001'
    HOST_URL: process.env.HOST_URL || 'http://flask:5000'
    
  },
  // Disable server-side rendering: https://go.nuxtjs.dev/ssr-mode
  ssr: false,

  // Target: https://go.nuxtjs.dev/config-target
  target: 'static',

  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    titleTemplate: '%s - ipocc',
    title: 'ipocc',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' },
      { name: 'format-detection', content: 'telephone=no' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ]
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: [
    'vue-json-pretty/lib/styles.css'
  ],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [
    '@/plugins/vue-json-pretty'
  ],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
    // https://go.nuxtjs.dev/eslint
    '@nuxtjs/eslint-module',
    // https://go.nuxtjs.dev/vuetify
    '@nuxtjs/vuetify',
  ],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    // https://go.nuxtjs.dev/axios
    '@nuxtjs/axios',
    // https://go.nuxtjs.dev/pwa
    '@nuxtjs/pwa',
  ],

  // Axios module configuration: https://go.nuxtjs.dev/config-axios
  axios: {
    // proxy: true,
    // baseURL: 'http://localhost:3001',// local開発時
    // baseURL: 'http://flask:5000',// docker組込み時

    proxy: true,
  },
  proxy: {
    // "/api/": process.env.API_URL || "http://localhost:3001/",
    // "/hello": process.env.API_URL || "http://localhost:3001/hello",
    // "/hello/": "http://localhost:3001/hello",
    "/hello": {
      // target: "http://localhost:3001/hello",
      target: "http://flask:5000/hello",
      pathRewrite: { "^/hello": "" },
    },
  },

  // PWA module configuration: https://go.nuxtjs.dev/pwa
  pwa: {
    manifest: {
      lang: 'en'
    }
  },

  // Vuetify module configuration: https://go.nuxtjs.dev/config-vuetify
  vuetify: {
    customVariables: ['~/assets/variables.scss'],
    theme: {
      dark: true,
      themes: {
        dark: {
          primary: colors.blue.darken2,
          accent: colors.grey.darken3,
          secondary: colors.amber.darken3,
          info: colors.teal.lighten1,
          warning: colors.amber.base,
          error: colors.deepOrange.accent4,
          success: colors.green.accent3
        }
      }
    }
  },

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {
    // https://qiita.com/hiroyukiwk/items/b283ef5312b289be6ce8
    babel: {
      plugins: [
        // https://stackoverflow.com/questions/68663581/latest-nuxt-v2-15-7-install-with-babel-loose-option-warnings
        // '@babel/plugin-proposal-class-properties',
        // '@babel/plugin-proposal-private-methods',
  
        // or with JUST the line below 
        ['@babel/plugin-proposal-private-property-in-object', { loose: true }]
      ],
    },
  },
  
  // https://sunday-morning.app/posts/2020-11-30-docker-nuxt-js-hot-reload
  watchers: {
    webpack: {
      poll: true
    }
  },
  // env: {
  //   HOST_URL: process.env.HOST_URL || 'http://localhost:3001'
  //   // HOST_URL: process.env.HOST_URL || 'http://flask:5000'
  // },
}
