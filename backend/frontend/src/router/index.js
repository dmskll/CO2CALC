import { createRouter, createWebHistory } from "vue-router";
import HomeView from '../views/HomeView.vue'
import InfoView from '../views/InfoView.vue'


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
    }
]

const router = createRouter({
    history: createWebHistory('/'),
    routes
})

export default router