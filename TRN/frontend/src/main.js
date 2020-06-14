
import 'bootstrap-vue/dist/bootstrap-vue.css';
import 'bootstrap/dist/css/bootstrap.css';
import 'vue-datetime/dist/vue-datetime.css'

import Vue from 'vue'

import axios from 'axios'
import App from './App.vue'
import BootstrapVue from 'bootstrap-vue';
import { Datetime } from 'vue-datetime'
import moment from 'moment'
import router from './router'
import store from './store'

Vue.config.productionTip = false

Vue.use(BootstrapVue);
Vue.use(Datetime)

axios.defaults.baseURL = 'http://127.0.0.1:8000';
if (localStorage.getItem('token')) {
  axios.defaults.headers.common['Authorization'] = `Token ${localStorage.getItem('token')}`;
}

Vue.filter('formatDate', function(value) {
  if (value) {
    return moment(String(value)).format('DD/MM/YYYY hh:mm')
  }
});

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (!store.getters.isAuthenticated) {
      next({ name: 'login' })
    } else {
      next()
    }
  } else {
    next()
  }
})

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
