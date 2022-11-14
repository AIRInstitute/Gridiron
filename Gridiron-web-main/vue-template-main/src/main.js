import 'bootstrap-css-only/css/bootstrap.min.css'
import 'mdbvue/lib/css/mdb.min.css'
import { createApp } from 'vue'
import { Vue3Mq } from "vue3-mq";
import { createPinia } from 'pinia'
//import { pinia } from 'Partials/Table/user.js';
import App from './App.vue'
import { ref } from 'vue';
import router from './router'
import 'bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import $ from "jquery";



// const cors = require('cors');
const pinia = createPinia()
window.$ = $

var CONFIG = require('./config_themes.json');
let app = createApp(App)

/* Get all partners logos */
var partners = []
const result = require.context(
    '@/assets/partners/',
    true,
    /^.*\./
)
for (var i = 0; i < result.keys().length; i++) {
    var s = result.keys()[i].substring(1);
    partners.push(s.substring(1))
}
/* ------ Config ------ */
app.config.globalProperties.$logged_in = false
app.config.globalProperties.partners = partners
app.config.globalProperties.footerCopyRight = CONFIG.footerCopyRight
app.config.globalProperties.projectName = CONFIG.projectName
app.config.globalProperties.projectSubtitle = CONFIG.projectSubtitle
app.config.globalProperties.primaryColor = CONFIG.primaryColor
app.config.globalProperties.secondaryColor = CONFIG.secondaryColor
app.config.globalProperties.primaryFont = CONFIG.primaryFont
app.config.globalProperties.secondaryFont = CONFIG.secondaryFont
app.config.globalProperties.url = CONFIG.api_url
app.config.globalProperties.projectLogo = require('@/assets/logo.png');
app.config.globalProperties.Global_noLiquid = require('@/assets/noLiquid.png');
app.config.globalProperties.Global_Liquid = require('@/assets/Trypan blue.png');
app.config.globalProperties.backgroundImg = require('@/assets/background-img.jpg');
app.config.globalProperties.KEYROCK_URL = "212.128.140.209:3005"
// app.use(cors)
  
/* ------ End of config ------ */
app.use(pinia)
app.use(router)
app.use(Vue3Mq, {
    breakpoints: { desktop: 0 }
})

const vm = app.mount('#app')
