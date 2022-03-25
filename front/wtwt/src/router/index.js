import { createRouter, createWebHashHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Connexion from "../views/Connexion";
import Inscription from "../views/Inscription";
import Preferences from "../views/Preferences";
import Groupe from "../views/Groupe";

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
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
  }
]

const router = createRouter({
  mode:"history",
  history: createWebHashHistory(),
  routes
})

export default router