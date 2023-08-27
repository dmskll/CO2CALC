import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import { createPinia } from 'pinia'

import 'katex/dist/katex.min.css'
import VueKatex from '@hsorby/vue3-katex'

import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'

// /* import the fontawesome core */
// import { library } from '@fortawesome/fontawesome-svg-core'
// /* import font awesome icon component */
// import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
// /* import specific icons */
// import { icons_solid } from '@fortawesome/free-solid-svg-icons'
// // import { icons_regular } from '@fortawesome/free-regular-svg-icons'
// /* add icons to the library */
// library.add(icons_solid)

import { library } from "@fortawesome/fontawesome-svg-core";
import { faFileCirclePlus, faCircleInfo} from "@fortawesome/free-solid-svg-icons";
import { faFolderOpen } from "@fortawesome/free-regular-svg-icons";
library.add(faFolderOpen, faFileCirclePlus, faCircleInfo);
// library.add(folderOpen);
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";

const pinia = createPinia()
const app = createApp(App)

app.use(pinia)
app.use(ElementPlus)
app.use(VueKatex)
app.use(router).mount('#app')
app.component('font-awesome-icon', FontAwesomeIcon)

import { useComponentsData } from "@/stores/ComponentsData"
const store = useComponentsData();
console.log(store.components)

