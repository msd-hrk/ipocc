// https://reffect.co.jp/vue/nuxt-js-vue-chartjs-easy-to-use
<template>
  <div>
    <h1>vue-chartjsで折れ線グラフ</h1>
    <LineChart />
  </div>
</template>

<script>
import LineChart from '@/components/LineChart.vue'

export default {
  components: {
    LineChart
  }
}
</script>