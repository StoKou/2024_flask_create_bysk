<!-- Contact.vue -->
<template>
  <div class="contact-page">
    <h1>联系我们</h1>
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
      <button type="submit">提交</button>
    </form>
    <div v-if="submitted">
      <p>您的信息已成功发送！我们将尽快回复您。</p>
    </div>
    <div v-if="error" class="error">
      {{ errorMessage }}
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
    name:'ContactPage',
  data() {
    return {
      formData: {
        name: '',
        email: '',
        message: '',
      },
      submitted: false,
      error: false,
      errorMessage: '',
    };
  },
  methods: {
    async onSubmit() {
      this.submitted = false;
      this.error = false;

      try {
        // 模拟向服务器发送请求
        const response = await axios.post('/api/contact', this.formData);
        if (response.status === 200) {
          this.submitted = true;
        } else {
          throw new Error('服务器响应异常');
        }
      } catch (error) {
        this.error = true;
        this.errorMessage = '发送失败，请稍后再试...';
        console.error('Error submitting contact form:', error);
      }
    },
  },
};
</script>

<style scoped>
/* 样式代码 */
.error {
  color: red;
}
</style>