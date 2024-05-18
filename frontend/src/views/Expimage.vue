<!-- Expimage.vue -->

<template>
  <div class="expimage-page">
    <header>
      <h1>实验图像数据</h1>
    </header>
    <section class="expimage-content">
      <div v-if="loading">
        <p>正在加载实验图像数据...</p>
      </div>
      <div v-else>
        <table border="1">
          <thead>
            <tr>
              <th>时间</th>
              <th>数值</th>
            </tr>
          </thead>
          <tbody>
            <!-- 使用 v-for 遍历 time 和 values 数组 -->
            <tr v-for="(index, time) in data.time" :key="index">
              <td>{{ time }}</td>
              <td>{{ data.values[index] }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'ExpimagePage',
  data() {
    return {
      loading: true,
      data: {
        time: [],
        values: [],
      },
    };
  },
  async created() {
    try {
      const response = await axios.get('/api/expimage/get_1');
      // 直接将返回的数据赋值给组件的data
      this.data = response.data;
      this.loading = false;
    } catch (error) {
      console.error('Error fetching experiment image data:', error);
      this.loading = false;
      // 可选：显示错误提示
      alert('无法获取实验图像数据，请稍后再试...');
    }
  },
};
</script>

<style scoped>
.expimage-page {
  /* 样式代码 */
}
</style>