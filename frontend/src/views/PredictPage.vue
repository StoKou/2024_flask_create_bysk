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
import { ref } from "vue";

export default {
  name: "PredictPage",
  setup() {
    const fileInput = ref(null);
    const loading = ref(false);
    const result = ref("");
    const selectedModel = ref("model1");

    const onFileChange = (event) => {
      // Simulate storing the selected file
      const selectedFile = event.target.files[0];
      console.log("Selected file:", selectedFile.name);
    };

    async function handleFormSubmit() {
      loading.value = true;
      try {
        const formData = new FormData();
        formData.append("file", fileInput.value.files[0]);

        let response;
        if (selectedModel.value === "model1") {
          response = await fetch("/api/predict/model_1", {
            method: "POST",
            body: formData,
          });
        } else {
          response = await fetch("/api/predict/model_2", {
            method: "POST",
            body: formData,
          });
        }

        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }

        result.value = await response.text();
        console.log("Prediction result:", result.value);

        // Artificial delay to simulate API request latency
        await new Promise((resolve) => setTimeout(resolve, 2000));

        loading.value = false;
      } catch (error) {
        console.error("Error simulating prediction:", error);
        loading.value = false;
        alert("模拟预测失败，请检查上传的文件格式或稍后再试...");
      }
    }

    // Interpret the numeric result into an emotional state
    // Interpret the numeric result into an emotional state
    function interpretResult() {
      const emotionalState =
        parseInt(result.value, 10) >= 0 && parseInt(result.value, 10) <= 2
          ? "0" === result.value
            ? "难过"
            : "1" === result.value
            ? "中性"
            : "开心"
          : "未知结果";

      // Log the raw result to the console
      console.log("Raw result from backend:", result.value);

      // Return an object with both the raw and interpreted results
      return { raw: result.value, interpreted: emotionalState };
    }

    return {
      fileInput,
      loading,
      result,
      handleFormSubmit,
      onFileChange,
      selectedModel,
      interpretResult, // Expose the function to the template
    };
  },
};
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