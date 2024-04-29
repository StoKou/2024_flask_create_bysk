<template>
  <div class="about-page">
    <header class="page-header">
      <h1 class="title">关于我们</h1>
    </header>
    <section class="about-content content-container">
      <h2 class="content-title">{{ aboutInfo.title }}</h2>
      <p class="description" v-html="aboutInfo.description"></p>
      
      <!-- 如果有团队成员信息或其他静态内容，可以在这里添加 -->
      <ul v-if="aboutInfo.teamMembers && aboutInfo.teamMembers.length > 0" class="team-members">
        <li v-for="(member, index) in aboutInfo.teamMembers" :key="index" class="team-member">
          <h3 class="member-name">{{ member.name }}</h3>
          <p class="member-role">{{ member.role }}</p>
        </li>
      </ul>
    </section>
  </div>
</template>

<script>
export default {
  name: 'AboutPage',
  data() {
    return {
      aboutInfo: {
        title: '关于我们标题',
        description: '这是一个关于我们页面的简短描述，采用静态数据填充。',
        teamMembers: [
          { name: '张三', role: '项目经理' },
          { name: '李四', role: '技术主管' },
          // 其他团队成员...
        ],
      },
    };
  },
};
</script>

<style scoped>
.about-page {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  min-height: 100vh; /* 使页面高度至少为视窗高度 */
}

.page-header {
  text-align: center;
}

.content-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 80%; /* 根据实际情况调整宽度 */
  max-width: 800px; /* 最大宽度限制 */
  padding: 2rem;
  box-sizing: border-box;
}

.title,
.content-title {
  text-align: center;
}

.description {
  text-align: justify;
  margin-bottom: 1rem;
}

.team-members {
  list-style: none;
  padding: 0;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

.team-member {
  margin: 1rem;
}
</style>