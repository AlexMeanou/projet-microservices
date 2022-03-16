import { createRouter, createWebHashHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Connexion from "../views/Connexion";

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/connexion',
    name: 'Connexion',
    component: Connexion
  }
]

const router = createRouter({
  mode:"history",
  history: createWebHashHistory(),
  routes
})

export default router