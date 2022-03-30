import { createApp } from 'vue'
import router from './router'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import axios from 'axios'
import VueAxios from 'vue-axios'
import { loadFonts } from './plugins/webfontloader'
import store from './store'

loadFonts()

const app = createApp(App)
app.use(router);
app.use(store);
app.use(vuetify);
app.use(VueAxios,axios);
app.mount('#app');
