import { createRouter, createWebHashHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Connexion from "../views/Connexion";
import Inscription from "../views/Inscription";
import Preferences from "../views/Preferences";
import Groupe from "../views/Groupe";
import Film from "../views/Film";
import LoginVue from '@/views/Login.vue';
import store from '../store/index';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
    meta : {
      requiresLogin : true
    }
  },
  {
    path: '/film/:id?',
    name: 'Film',
    component: Film,
    meta : {
      requiresLogin : true
    }
  },
  {
    path: '/preferences',
    name: 'Preferences',
    component: Preferences,
    meta : {
      requiresLogin : true
    }
  },
  {
    path: '/groupe',
    name: 'Groupe',
    component: Groupe,
    meta : {
      requiresLogin : true
    }
  },
  {
    path: '/connexion',
    name: 'Connexion',
    component: Connexion,
    meta : {
      requiresLogin : false
    }
  },
  {
    path: '/inscription',
    name: 'Inscription',
    component: Inscription,
    meta : {
      requiresLogin : false
    }
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginVue,
    meta : {
      requiresLogin : false
    }
  }
]

const router = createRouter({
  mode:"history",
  history: createWebHashHistory(),
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresLogin)) {
    if (store.getters.isLogged) {
      next()
    }else {
      next({ name: 'Login' })
    }
  } else {
    next()
  }
})

export default router