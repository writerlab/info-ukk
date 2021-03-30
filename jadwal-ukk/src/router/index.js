import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Lab1 from '@/components/Lab1'
import Lab2 from '@/components/Lab2'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/lab1',
      name: 'Lab1',
      component: Lab1
    },
    {
      path: '/lab2',
      name: 'Lab2',
      component: Lab2
    },
  ]
})
