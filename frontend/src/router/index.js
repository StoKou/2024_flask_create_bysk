// router/index.js 或 router/index.ts
import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue';
import About from '../views/About.vue';
import Contact from '../views/Contact.vue';
import Expimage from '../views/Expimage.vue';
import Echartsdemo from '../views/Echartsdemo.vue';
import PredictPage from '../views/PredictPage.vue'

const routes = [
  { path: '/', component: Home },
  { path: '/about', component: About },
  { path: '/contact', component: Contact },
  //
  { path: '/expimage', component: Expimage },
  { path: '/Echartsdemo', component: Echartsdemo },
  { path: '/PredictPage', component: PredictPage },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;