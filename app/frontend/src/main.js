import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import { createPinia } from 'pinia'


// import 'element-plus/dist/index.css'

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

import { faFileCirclePlus} from "@fortawesome/free-solid-svg-icons/faFileCirclePlus";
import { faCalculator} from "@fortawesome/free-solid-svg-icons/faCalculator";
import { faCircleInfo } from "@fortawesome/free-solid-svg-icons/faCircleInfo";
import { faPlus } from "@fortawesome/free-solid-svg-icons/faPlus";
import { faPlusSquare } from "@fortawesome/free-solid-svg-icons/faPlusSquare";
import { faMicrochip } from "@fortawesome/free-solid-svg-icons/faMicrochip";
import {  faBolt } from "@fortawesome/free-solid-svg-icons/faBolt";

import { faFilePdf } from "@fortawesome/free-regular-svg-icons/faFilePdf";
import { faFolderOpen } from "@fortawesome/free-regular-svg-icons/faFolderOpen";
import { faCircleQuestion } from "@fortawesome/free-regular-svg-icons/faCircleQuestion";


library.add(faFolderOpen, faBolt, faCircleQuestion, faCalculator, faFileCirclePlus, faCircleInfo, faPlusSquare, faPlus, faMicrochip, faFilePdf);
// library.add(folderOpen);
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";

const pinia = createPinia()
const app = createApp(App)


// import ElementPlus from 'element-plus'
// import 'element-plus/dist/index.css'
// app.use(ElementPlus)



app.use(pinia)
app.use(router).mount('#app')
app.component('font-awesome-icon', FontAwesomeIcon)

import { useComponentsData } from "@/stores/ComponentsData"
const store = useComponentsData();
console.log(store.components)

