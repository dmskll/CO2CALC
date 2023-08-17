import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import { createPinia } from 'pinia'

import 'katex/dist/katex.min.css'
import VueKatex from '@hsorby/vue3-katex'


import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'

const pinia = createPinia()
const app = createApp(App)

app.use(pinia)
app.use(ElementPlus)
app.use(VueKatex)
app.use(router).mount('#app')

import { useComponentsData } from "@/stores/ComponentsData"
const store = useComponentsData();
console.log(store.components)

