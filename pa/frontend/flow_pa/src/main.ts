import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import './assets/main.css'
import './styles/base/_reset.css'
import './styles/base/_variables.css'
import './styles/theme.css'

const app = createApp(App)
app.use(router)
app.mount('#app')
