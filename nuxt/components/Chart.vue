<script>
// https://zenn.dev/ryusou/articles/nuxt-chartjs
// import { Line, mixins } from 'vue-chartjs'
import { Line } from 'vue-chartjs'
// const { reactiveProp } = mixins

export default {
  extends: Line,
  // mixins: [reactiveProp],
  props: {
    chartData: {
      type: Object,
      default: null
    },
    options: {
      type: Object,
      default: null
    }
  },
  data(){
    return {
        // chartdata: {
        //     labels: ['January', 'February'],
        //     datasets: [
        //         {
        //         label: ['Data One'],
        //         data: [40, 30],
        //         backgroundColor: '#f87979',
        //         borderColor: '#f87979',
        //         fill: false, // not filling with background color
        //         }
        //     ]
        // },
        // options: {
        //     responsive: true,
        //     maintainAspectRatio: false
        // }
    }
  },
  mounted() {
    this.renderChart(this.chartData, this.options)
  }
}
</script>