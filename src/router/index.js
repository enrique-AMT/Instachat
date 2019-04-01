import Vue from 'vue'
import Router from 'vue-router'
import LoginScreen from '@/components/LoginScreen'
import HomeScreen from '@/components/HomeScreen'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/login',
      name: 'LoginScreen',
      component: LoginScreen
    },
    {
      path: '/home',
      name: 'HomeScreen',
      component: HomeScreen
    }
  ]
})
