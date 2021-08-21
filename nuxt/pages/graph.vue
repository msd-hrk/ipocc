<template>
  <div>
    <div class="chart-container">
      <h1>chart</h1>
      <chart
        :chartData="chartData"
        :options="options"
      />
    </div>

    <p>
      info.priceDiary
      <br>
      {{info.priceDiary}}
    </p>
    <br>
    {{info}}
  </div>
</template>
<script>
import chart from '../components/Chart'

export default {
  components: { chart },

  // https://ja.nuxtjs.org/docs/2.x/features/data-fetching
  async asyncData({ store }) {
    await store.dispatch('getHello')
  },

  data () {
    return{
      info:'',
    }
  },
  created(){
    // this.$store.dispatch('getHello')
    // this.getHello()
    this.info = this.$store.state.info; // store/index.jsのstate.statusを取得
    console.log(this.info)

// 確認用
    this.priceDiaryDate()
    this.priceDiaryAmt()
    // this.priceDiaryLabel()
// 確認用
    this.createChart()
  },
  mounted(){
  },
  methods:{
    priceDiaryDate(){
      const date = this.info.priceDiary.map(element => element[0])
      console.log(date)
      return date
    },
    // priceDiaryTime(){
    //   const time = this.info.priceDiary.map(element => element[0])
    //   console.log(time)
    //   return time
    // },
    priceDiaryAmt(){
      const firstAmount = this.info.priceDiary.map(element => element[1])
      console.log(firstAmount)
      return firstAmount
    },
    createChart(){
      this.chartData = {
        labels: this.priceDiaryDate(),
        // labels: ['2021/08/12','2021/08/13'],
        datasets: [
          {
            // label: "フォロー",
            label: "primaryDiary",
            backgroundColor: 'rgb(232, 234, 246, 0.1)',
            borderColor: "#C5CAE9",
            // data: [0,1],
            data: this.priceDiaryAmt(),
            fill: true
          },
          {
            label: "test",
            backgroundColor: 'rgb(232, 234, 246, 0.1)',
            borderColor: "#C5CAE9",
            // data: [0,1],
            data: [100,200,300,400,500],
            fill: true
          }
        ]
      }
      this.options = {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          y: {
            stacked: true,
            ticks: {
              color: "#E8EAF6",
            },
            grid: {
              color: "rgb(232, 234, 246, 0.1)"
            },
          },
          x: {
            ticks: {
              color: "#E8EAF6",
            },
            grid: {
              color: "rgb(232, 234, 246, 0.1)"
            }
          }
        }
      }
    }
  }
}
</script>