// main.js
import { createApp } from 'vue';
import App from './App.vue';
import router from './router'; // 引入刚才创建的路由实例
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';

Vue.use(ElementUI);

// 创建并配置 Vue 应用
const app = createApp(App);


// 注册全局路由
app.use(router);

// 挂载应用到 #app 元素
app.mount('#app');