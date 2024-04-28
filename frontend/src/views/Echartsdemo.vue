<template>
  <!-- Vue组件模板 -->
  <div id="app">
    <!-- 定义一个div作为ECharts图表容器，通过ref属性绑定到Vue实例上 -->
    <div ref="chart" style="width: 100%; height: 400px;"></div>
  </div>
</template>

<script>
// 导入ECharts库和Axios库
import * as echarts from 'echarts';
import axios from 'axios';

// 定义Vue组件
export default {
  // 给组件命名
  name: 'LineChartComponent',

  // 初始化组件状态数据
  data() {
    return {
      // 存储ECharts实例的引用
      chartInstance: null,
      // 存储图表配置项
      chartOptions: {},
      // 存储类别标签数据
      categories: [],
      // 存储数值型数据
      values: [],
    };
  },

  // 在组件挂载完成后执行fetchData方法获取数据
  mounted() {
    this.fetchData();
  },

  // 定义组件的方法
  methods: {
    // 异步获取数据的方法
    async fetchData() {
      try {
        // 使用Axios发送GET请求到'/api/expimage'接口
        const response = await axios.get('/api/expimage');

        // 如果请求成功并且返回了有效数据
        if (response.data) {
          // 将接收到的类别数据赋值给categories
          this.categories = response.data.categories;
          // 将接收到的数值数据赋值给values
          this.values = response.data.values;

          // 数据准备好后初始化并绘制图表
          this.initChart();
        }
      } catch (error) {
        // 如果请求过程中发生错误，打印错误信息
        console.error('Error fetching data:', error);
      }
    },

    // 初始化并设置ECharts图表的方法
    initChart() {
      // 使用ECharts初始化图表实例，传入已绑定的DOM元素ref="chart"
      this.chartInstance = echarts.init(this.$refs.chart);

      // 设置图表的基本配置项，包括x轴（类别轴）、y轴（数值轴）和折线图系列数据
      this.chartOptions = {
        xAxis: {
          type: 'category', // x轴类型为分类轴
          data: this.categories, // x轴数据来自this.categories
        },
        yAxis: {
          type: 'value', // y轴类型为数值轴
        },
        series: [
          {
            // 折线图系列数据
            data: this.values, 
            type: 'line', // 图表类型为折线图
          },
        ],
      };

      // 设置ECharts实例的配置选项并更新图表
      this.chartInstance.setOption(this.chartOptions);
    },
  },
};

</script>

<style scoped>
/* CSS样式部分，只针对本组件内部生效 */
#app {
  /* 中心垂直和水平居中布局 */
  display: flex;
  justify-content: center;
  align-items: center;
  /* 组件高度充满整个视窗 */
  height: 100vh;
}
</style>