import { createRouter, createWebHistory } from "vue-router";
// import HomeView from '../views/HomeView.vue'
// import InfoView from '../views/InfoView.vue'
// import ReportView from '../views/ReportView.vue'
// import ComponentsView from '../views/ComponentsView.vue'



const routes = [
    {
        path: '/',
        name: 'Home',
        component: () => import('../views/HomeView.vue')
    },
    {
        path: '/info',
        name: 'Info',
        component: () => import('../views/InfoView.vue')
    },
    {
        path: '/components',
        name: 'Components',
        component: () => import('../views/ComponentsView.vue')
    },
    {
        path: '/report',
        name: 'Report',
        component: () => import('../views/ReportView.vue')
    }
]

const router = createRouter({
    history: createWebHistory('/'),
    routes
})

export default router