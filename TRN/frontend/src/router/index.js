import Vue from 'vue'
import VueRouter from 'vue-router'

import AuthView from '../views/AuthView.vue'
import TournamentsListView from '../views/TournamentsListView'
import TournamentCreateView from '../views/TournamentCreateView'
import TournamentView from '../views/TournamentView'
import TournamentUpdateView from '../views/TournamentUpdateView'
import UserTournamentsListView from '../views/UserTournamentsListView'
import ConfirmEmailView from '../views/ConfirmEmailView'

Vue.use(VueRouter)

const routes = [
  {
    path: '/login',
    name: 'Auth',
    component: AuthView
  },
  {
    path: '/',
    name: 'Tournaments',
    component: TournamentsListView
  },
  {
    path: '/tournaments/user',
    name: 'UserTournamentsList',
    component: UserTournamentsListView
  },
  {
    path: '/tournaments/create',
    name: 'TournamentsCreate',
    component: TournamentCreateView,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/tournament/:id',
    name: 'Tournament',
    component: TournamentView
  },
  {
    path: '/tournament/:id/update',
    name: 'TournamentUpdate',
    component: TournamentUpdateView
  },
  {
    path: '/confirm/:uidb64/:token',
    name: 'ConfirmEmail',
    component: ConfirmEmailView
  }
]

const router = new VueRouter({
  linkExactActiveClass: 'link-active',
  mode: 'history',
  routes
})

export default router
