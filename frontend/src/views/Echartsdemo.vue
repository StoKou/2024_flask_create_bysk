<template>
  <div id="app">
    <!-- 添加一个标题显示name -->
    <h1 v-if="chartOptions.name">{{ chartOptions.name }}</h1>
    <!-- 定义一个div作为ECharts图表容器，通过ref属性绑定到Vue实例上 -->
    <div ref="chart" style="width: 100%; height: 400px;"></div>
    <!-- 添加目录选择器 -->
    <select v-model="selectedCategory" @change="handleCategoryChange">
      <option disabled value="">请选择目录</option>
      <option v-for="category in categories" :key="category">{{ category }}</option>
    </select>
    <!-- 添加刷新按钮 -->
    <button @click="fetchData">刷新</button>
  </div>
</template>

<script>
// 导入ECharts库和Axios库
import * as echarts from 'echarts';
import axios from 'axios';

export default {
  name: 'LineChartComponent',
  data() {
    return {
      chartInstance: null,
      chartOptions: { name: '' },
      categories: [],
      values: [],
      selectedCategory: '', // 用于v-model绑定的目录选择器
    };
  },
  mounted() {
    this.fetchData();
  },
  methods: {
    async fetchData() {
      try {
        const response = await axios.get('/api/expimage/get_1', {
          params: { category: this.selectedCategory } // 传递选中的目录作为参数
        });
        if (response.data) {
          this.chartOptions.name = response.data.name; // 设置图表名称
          this.categories = response.data.categories;
          this.values = response.data.values;
          this.initChart();
        }
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    },
    initChart() {
      this.chartInstance = echarts.init(this.$refs.chart);
      this.chartOptions = {
        title: { text: this.chartOptions.name }, // 设置图表标题
        xAxis: { type: 'category', data: this.categories },
        yAxis: { type: 'value' },
        series: [{ data: this.values, type: 'line' }],
      };
      this.chartInstance.setOption(this.chartOptions);
    },
    handleCategoryChange() {
      this.fetchData(); // 当目录改变时重新获取数据
    },
  },
};

</script>

<style scoped>
#app {
  display: flex;
  flex-direction: column;
  align-items: center;
  height: 100vh;
  justify-content: space-around;
}
h1 {
  margin-bottom: 20px; /* 给标题一些空间 */
}
</style>