<template>
  <div id="app">
    <nav>
      <router-link to="/">首页</router-link>
      <router-link to="/about">关于我们</router-link>
      <router-link to="/contact">联系我们</router-link>
      <router-link to="/expimage">实验图像</router-link>
      <router-link to="/echartsdemo">测试模块</router-link>
      <router-link to="/predictpage">预测</router-link>
    </nav>
    <router-view />
  </div>
</template>

<style scoped>
/* 样式代码 */
nav {
  display: flex;
  justify-content: space-around;
  background-color: #f0f0f0;
  padding: 10px;
}

router-link {
  text-decoration: none;
  color: #333;
  font-weight: bold;
  transition: color 0.3s;
}

router-link:hover {
  color: #007bff;
}
</style>
