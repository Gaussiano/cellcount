<script setup lang="ts">
import { ref } from 'vue'

const result = ref<any>(null)
const loading = ref(false)
const error = ref<string | null>(null)

async function run() {
  loading.value = true
  error.value = null
  try {
    result.value = await (window as any).api.runPipeline('pipelines/hello.yaml')
  } catch (e: any) {
    error.value = e.message
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <main>
    <h1>CellCount</h1>
    <button @click="run" :disabled="loading">
      {{ loading ? 'Running...' : 'Run hello pipeline' }}
    </button>
    <p v-if="error" class="error">{{ error }}</p>
    <table v-if="result">
      <thead>
        <tr>
          <th v-for="c in result.columns" :key="c">{{ c }}</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(row, i) in result.rows" :key="i">
          <td v-for="(cell, j) in row" :key="j">{{ cell }}</td>
        </tr>
      </tbody>
    </table>
  </main>
</template>

<style scoped>
main {
  padding: 32px;
  font-family: sans-serif;
}
h1 {
  margin-bottom: 24px;
  font-size: 2rem;
}
button {
  padding: 10px 24px;
  font-size: 1rem;
  cursor: pointer;
  background: #4f8ef7;
  color: white;
  border: none;
  border-radius: 6px;
  margin-bottom: 24px;
}
button:disabled {
  opacity: 0.5;
}
.error {
  color: #ff4444;
  margin-bottom: 16px;
}
table {
  border-collapse: collapse;
  width: 100%;
}
th, td {
  border: 1px solid #444;
  padding: 8px 16px;
  text-align: left;
}
th {
  background: #2a2a2a;
}
</style>