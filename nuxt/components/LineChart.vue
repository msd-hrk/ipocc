// https://reffect.co.jp/vue/nuxt-js-vue-chartjs-easy-to-use
<script>
import { Line } from 'vue-chartjs'
export default {
  extends: Line,
  data(){
    return {
        chartdata: {
            labels: ['January', 'February'],
            datasets: [
                {
                label: ['Data One'],
                data: [40, 30],
                backgroundColor: '#f87979',
                borderColor: '#f87979',
                fill: false, // not filling with background color
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