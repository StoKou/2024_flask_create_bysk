<template>
  <div class="home-page">
    <header class="header">
      <h1>2024创新实践小组</h1>
    </header>
    <main class="main-content">
      <div class="intro-section">
        <h2>组员：时扣、陈亮亮</h2>
        <p>going</p>
      </div>
      <div class="features">
        <div class="feature-item" v-for="item in features" :key="item.title">
          <img :src="item.image" alt="" class="feature-image" />
          <h3 class="feature-title">{{ item.title }}</h3>
          <p class="feature-description">{{ item.description }}</p>
        </div>
      </div>
    </main>
    <footer class="footer">
      <!-- 底部内容 -->
    </footer>
  </div>
</template>

<script>
export default {
  name: 'HomePage',
  data() {
    return {
      features: [
        {
          title: '特性一',
          description: '这是特性一的描述。',
          image: '/path/to/image1.png'
        },
        {
          title: '特性二',
          description: '这是特性二的描述。',
          image: '/path/to/image2.png'
        },
        {
          title: '特性三',
          description: '这是特性三的描述。',
          image: '/path/to/image3.png'
        }
        // 更多特性...
      ],
    };
  },
  // 删除created钩子，因为它用于从后端获取数据
  // created() {
  //   ...
  // },
};
</script>


<style scoped>
.home-page {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  background: url('/public/images/1.png') no-repeat center center fixed;
  background-size: cover;
  color: #212529;
  font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
  /* 其他样式 */
}

.header {
  padding: 2rem;
  text-align: center;
}

.main-content {
  flex: 1;
  padding: 2rem;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.intro-section {
  max-width: 800px;
  margin-bottom: 2rem;
  text-align: center;
}

.features {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
}

.feature-item {
  flex: 1;
  max-width: 30%;
  margin: 1rem;
  padding: 1rem;
  background: white;
  border-radius: 10px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  text-align: center;
}

.feature-image {
  max-width: 100%;
  height: auto;
  border-radius: 5px;
}

.feature-title {
  margin-top: 0.5rem;
  font-size: 1.2rem;
  color: #333;
}

.feature-description {
  color: #666;
  line-height: 1.5;
}

.footer {
  padding: 1rem;
  background: #eef0f3;
  text-align: center;
}

/* 响应式设计 */
@media (max-width: 768px) {
  .feature-item {
    max-width: 45%;
  }
}

@media (max-width: 480px) {
  .feature-item {
    max-width: 100%;
  }
}
</style>