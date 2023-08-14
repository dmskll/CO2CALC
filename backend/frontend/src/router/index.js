import { createRouter, createWebHistory } from "vue-router";
import HomeView from '../views/HomeView.vue'
import InfoView from '../views/InfoView.vue'
import ReportView from '../views/ReportView.vue'
import ComponentsView from '../views/ComponentsView.vue'



const routes = [
    {
        path: '/',
        name: 'Home',
        component: HomeView
    },
    {
        path: '/info',
        name: 'Info',
        component: InfoView
    },
    {
        path: '/components',
        name: 'Components',
        component: ComponentsView
    },
    {
        path: '/report',
        name: 'Report',
        component: ReportView
    }
]

const router = createRouter({
    history: createWebHistory('/'),
    routes
})

export default router