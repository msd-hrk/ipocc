// https://reffect.co.jp/vue/nuxt-js-vue-chartjs-easy-to-use
<script>
import { Bar } from 'vue-chartjs'
export default {
  extends: Bar,
  data(){
    return {
        chartdata: {
            labels: ['January', 'February'],
            datasets: [
                {
                label: ['Data One'],
                backgroundColor: '#f87979',
                data: [40, 30]
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false
        }
    }
  },
  mounted () {
    this.renderChart(this.chartdata, this.options)
  }
}
</script>