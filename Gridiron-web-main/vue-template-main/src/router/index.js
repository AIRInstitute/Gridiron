import { createRouter, createWebHistory, createWebHashHistory } from 'vue-router'
import Home from '../views/Home'
import Login from '../views/Login'
import Dashboard from '../views/Dashboard'
import Profile from '../views/Profile'
import TestComponents from '../views/TestComponents'
import Form from '../views/Form'
import CRUD from '../views/CRUD'
import adminPanel from '../views/adminPanel'
import Protocols from '../views/Protocols'
import Microscope from '../views/Microscope'



const routes = [{
        path: '/',
        name: 'Home',
        component: Home,
    },
    {
        path: '/login',
        name: 'Login',
        component: Login,
    },
    {
        path: '/dashboard',
        name: 'Dashboard',
        component: Dashboard,
    },
    {
        path: '/profile',
        name: 'Profile',
        component: Profile,
    },
    {
        path: '/test',
        name: 'TestComponents',
        component: TestComponents,
    },
    {
        path: '/form',
        name: 'Form',
        component: Form,
    },
    {
        path: '/crud',
        name: 'CRUD',
        component: CRUD,
    },
    {
        path: '/adminPanel',
        name: 'AdminPanel',
        component: adminPanel,
    },
    {
        path: '/protocols',
        name: 'Protocols',
        component: Protocols,
    },
    {
        path: '/microscope',
        name: 'Microscope',
        component: Microscope,
    }
]

const router = createRouter({
    history: createWebHashHistory(process.env.BASE_URL),
    mode: 'hash',
    routes,
})

export default router