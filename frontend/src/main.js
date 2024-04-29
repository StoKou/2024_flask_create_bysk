// main.js
import { createApp } from 'vue';
import App from './App.vue';
import router from './router'; // 引入刚才创建的路由实例
// main.js 或你的应用入口文件



// 创建并配置 Vue 应用
const app = createApp(App);


// 注册全局路由
app.use(router);

// 挂载应用到 #app 元素
app.mount('#app');