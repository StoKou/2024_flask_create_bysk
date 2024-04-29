<!-- App.vue -->
<template>
  <div id="app">
    <!-- 若有全局导航或公用组件，可以在这里放置 -->
    <nav>
      <router-link to="/">首页</router-link> |
      <router-link to="/about">关于我们</router-link> |
      <router-link to="/contact">联系我们</router-link>
      <router-link to="/expimage">实验图像（excel图像测试阶段）</router-link>
      <router-link to="/echartsdemo">echarts</router-link>
      <br>
      <router-link to="/predictpage">predict</router-link>
    </nav>
    <!-- 路由视图，用于呈现匹配到的不同组件 -->
    <router-view />
  </div>
</template>

<script>


</script>

<style scoped>
/* 样式代码 */
</style>