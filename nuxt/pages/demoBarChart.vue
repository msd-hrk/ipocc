// https://reffect.co.jp/vue/nuxt-js-vue-chartjs-easy-to-use
<template>
  <div>
    <h1>vue-chartjsで棒グラフ</h1>
    <BarChart />
  </div>
</template>

<script>
import BarChart from '@/components/BarChart.vue'

export default {
  components: {
    BarChart
  }
}
</script>