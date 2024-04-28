<!-- About.vue -->

<template>
  <div class="about-page">
    <header>
      <h1>关于我们</h1>
    </header>
    <section class="about-content">
      <div v-if="loading">
        <p>正在加载关于我们信息...</p>
      </div>
      <div v-else>
        <h2>{{ aboutInfo.title }}</h2>
        <p v-html="aboutInfo.description"></p>
        <!-- 如果有团队成员信息或其他静态或动态内容，可以在这里添加 -->
        <ul v-if="aboutInfo.teamMembers">
          <li v-for="(member, index) in aboutInfo.teamMembers" :key="index">
            <h3>{{ member.name }}</h3>
            <p>{{ member.role }}</p>
          </li>
        </ul>
      </div>
    </section>
  </div>
</template>

<script>
import axios from 'axios';

export default {
    name:'AboutPage',
  data() {
    return {
      loading: true,
      aboutInfo: {
        title: '',
        description: '',
        teamMembers: [],
      },
    };
  },
  async created() {
    try {
      const response = await axios.get('/api/about'); // 假设这是获取关于信息的接口
      this.aboutInfo = response.data;
      this.loading = false;
    } catch (error) {
      console.error('Error fetching about information:', error);
      this.loading = false;
      this.aboutInfo = {
        title: '加载失败',
        description: '无法获取关于我们信息，请稍后再试...',
        teamMembers: [],
      };
    }
  },
};
</script>

<style scoped>
/* 样式代码 */
.about-page {
  /* 根据需要添加样式 */
}
</style>