<template>
  <div id="app">
    <!-- 优化过的原生导航栏 -->
    <nav class="custom-nav">
      <router-link to="/" class="nav-item">首页</router-link>
      <router-link to="/expimage" class="nav-item">图像</router-link>
      <router-link to="/echartsdemo" class="nav-item">测试</router-link>
      <router-link to="/predictpage" class="nav-item">预测</router-link>
      <router-link to="/about" class="nav-item">关于我们</router-link>
      <router-link to="/contact" class="nav-item">联系我们</router-link>
    </nav>
    
    <!-- 路由视图，用于呈现匹配到的不同组件 -->
    <router-view />
  </div>
</template>

<style scoped>
.custom-nav {
  display: flex;
  justify-content: space-around;
  align-items: center;
  height: 50px; /* 设置导航栏高度 */
  padding: 0 20px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* 添加阴影效果 */
  background-color: #f0f2f5; /* 设置背景颜色 */
}

.nav-item {
  color: #333;
  text-decoration: none;
  transition: all 0.3s ease;

  &:hover {
    color: #007bff; /* 鼠标悬停时的颜色 */
  }

  & + .nav-item {
    margin-left: 16px; /* 为相邻的 router-link 添加间距 */
  }
}
</style>