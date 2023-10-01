import { createRouter, createWebHistory } from "vue-router";




const routes = [
    {
        path: '/',
        name: 'Calculator',
        component: () => import('../views/CalculatorView.vue')
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