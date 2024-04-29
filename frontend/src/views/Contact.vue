<template>
  <div class="contact-page">
    <h1 class="contact-title">联系我们</h1>
    <div class="contact-info">
      <p>欢迎通过电子邮件与我们取得联系:</p>
      <a href="mailto:your-email@example.com" class="email-link">your-email@example.com</a>
    </div>
    <!-- 如果需要，可以在此处保留简洁的反馈表单，但去除提交功能 -->
    <div class="feedback-form" v-if="showFeedbackForm">
      <h2>快速反馈</h2>
      <form @submit.prevent="onSubmit">
        <div>
          <label for="name">姓名：</label>
          <input type="text" id="name" v-model="formData.name" required>
        </div>
        <div>
          <label for="email">邮箱：</label>
          <input type="email" id="email" v-model="formData.email" required>
        </div>
        <div>
          <label for="message">留言：</label>
          <textarea id="message" v-model="formData.message" required></textarea>
        </div>
        <button type="submit" disabled>提交（仅供演示）</button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ContactPage',
  data() {
    return {
      formData: {
        name: '',
        email: '',
        message: '',
      },
      showFeedbackForm: true, // 控制是否显示反馈表单，默认显示
    };
  },
  methods: {
    onSubmit() {
      alert('感谢您的反馈！请通过邮件联系我们。');
    },
  },
};
</script>

<style scoped>
/* 样式代码 */
.contact-page {
  text-align: center;
}

.contact-title {
  margin-bottom: 1rem;
}

.contact-info {
  margin-bottom: 2rem;
}

.email-link {
  color: #007bff;
  font-weight: bold;
  text-decoration: none;
}

.feedback-form {
  display: flex;
  flex-direction: column;
  align-items: center;
  max-width: 400px;
  margin: 0 auto;
}

.feedback-form label,
.feedback-form input,
.feedback-form textarea,
.feedback-form button {
  width: 100%;
  margin-bottom: 1rem;
}

.error {
  color: red;
}
</style>