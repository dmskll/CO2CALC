import { createRouter, createWebHistory } from "vue-router";
import HomeView from '../views/HomeView.vue'
import InfoView from '../views/InfoView.vue'
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
    }
]

const router = createRouter({
    history: createWebHistory('/'),
    routes
})

export default router