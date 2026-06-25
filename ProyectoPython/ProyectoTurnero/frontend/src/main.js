// Inicializa Vue, registra Pinia y activa el sistema de rutas.
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'
import './style.css'

const app = createApp(App)

// Pinia debe registrarse antes del router porque las vistas consumen el store.
app.use(createPinia())
app.use(router)

app.mount('#app')
