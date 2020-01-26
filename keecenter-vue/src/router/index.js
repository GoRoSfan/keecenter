import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import AllNews from '../views/AllNews';
import Legals from '../views/Legals';
import Contacts from '../views/Contacts';
import AllEvents from '../views/AllEvents';
import About from '../views/About';
import AllEmployees from '../views/AllEmployees'
import Partners from "../views/Partners";

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'home',
        component: Home
    },

    {
      path: '/news',
      name: 'all-news',
      component: AllNews,
    },

    {
      path: '/legal',
      name: 'legals',
      component: Legals,
    },

    {
      path: '/contact',
      name: 'contacts',
      component: Contacts,
    },

    {
      path: '/events',
      name: 'all-events',
      component: AllEvents,
    },

    {
      path: '/about',
      name: 'about',
      component: About,
    },

    {
      path: '/employees',
      name: 'employees',
      component: AllEmployees,
    },

    {
      path: '/partners',
      name: 'partners',
      component: Partners,
    }

    // {
    //   path: '/about',
    //   name: 'about',
    //   // route level code-splitting
    //   // this generates a separate chunk (about.[hash].js) for this route
    //   // which is lazy-loaded when the route is visited.
    //   component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
    // }
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router
