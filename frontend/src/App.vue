<template>
  <div id="app">
    <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" router>
      <el-menu-item index="/">首页</el-menu-item>
      <el-submenu index="1">
        <template slot="title">关于我们</template>
        <el-menu-item index="/about">公司介绍</el-menu-item>
        <el-menu-item index="/contact">联系我们</el-menu-item>
        <!-- 如果有更多子菜单项，可以继续添加 -->
      </el-submenu>
      <el-menu-item index="/expimage">实验图像</el-menu-item>
      <el-menu-item index="/echartsdemo">测试模块</el-menu-item>
      <el-menu-item index="/predictpage">预测</el-menu-item>
    </el-menu>
    <router-view />
  </div>
</template> 

<script>
import { Menu, MenuItem, Submenu } from 'element-ui';
import { useRouter } from 'vue-router';

export default {
  components: {
    [Menu.name]: Menu,
    [MenuItem.name]: MenuItem,
    [Submenu.name]: Submenu
  },
  setup() {
    const router = useRouter();
    const activeIndex = router.currentRoute.path;

    return {
      activeIndex
    };
  }
};
</script>

<style scoped>
.el-menu-demo {
  background-color: #f0f0f0;
}
</style>