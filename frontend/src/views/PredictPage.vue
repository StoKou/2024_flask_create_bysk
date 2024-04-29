<template>
  <div class="predict-page">
    <header class="page-header">
      <h1>实验数据预测</h1>
    </header>
    <section class="predict-content content-container">
      <form class="predict-form" @submit.prevent="handleFormSubmit">
        <div class="form-group">
          <input type="file" ref="fileInput" @change="onFileChange" />
          <label class="file-label">选择文件</label>
        </div>
        <div class="form-group">
          <label class="radio-label">
            <input
              type="radio"
              name="model"
              value="model1"
              v-model="selectedModel"
            />
            Model 1
          </label>
          <label class="radio-label">
            <input
              type="radio"
              name="model"
              value="model2"
              v-model="selectedModel"
            />
            Model 2
          </label>
        </div>
        <button type="submit" class="predict-button">确定</button>
      </form>
      <div v-if="loading" class="loading-message">
        <p>正在模拟预测...</p>
      </div>
      <div v-if="result && !loading" class="prediction-result">
        <h3>模拟预测结果：</h3>
        <p>原始结果：{{ interpretResult().raw }}</p>
        <p>解释结果：{{ interpretResult().interpreted }}</p>
      </div>
    </section>
  </div>
</template>

<script>
// ...原有 script 内容不变...
</script>

<style scoped>
.predict-page {
  display: flex;
  flex-direction: column;
  align-items: center;
  min-height: 100vh;
  padding: 2rem;
}

.page-header {
  text-align: center;
}

.content-container {
  width: 80%;
  max-width: 800px;
  display: flex;
  flex-direction: column;
  align-items: center;
  box-sizing: border-box;
}

.predict-form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.file-label {
  cursor: pointer;
  user-select: none;
}

.radio-label {
  display: inline-block;
  cursor: pointer;
}

.predict-button {
  width: 100%;
  padding: 0.5rem 1rem;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  text-align: center;
}

.loading-message {
  text-align: center;
  margin-top: 2rem;
}

.prediction-result {
  width: 100%;
  text-align: center;
  margin-top: 2rem;
}
</style>