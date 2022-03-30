import { createRouter, createWebHashHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Connexion from "../views/Connexion";
import Inscription from "../views/Inscription";
import Preferences from "../views/Preferences";
import Groupe from "../views/Groupe";
import Film from "../views/Film";
import LoginVue from '@/views/Login.vue';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/film/:id?',
    name: 'Film',
    component: Film
  },
  {
    path: '/preferences',
    name: 'Preferences',
    component: Preferences
  },
  {
    path: '/groupe',
    name: 'Groupe',
    component: Groupe
  },
  {
    path: '/connexion',
    name: 'Connexion',
    component: Connexion
  },
  {
    path: '/inscription',
    name: 'Inscription',
    component: Inscription
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginVue
  }
]

const router = createRouter({
  mode:"history",
  history: createWebHashHistory(),
  routes
})

export default router