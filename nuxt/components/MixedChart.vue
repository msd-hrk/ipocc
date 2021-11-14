<script>
// https://zenn.dev/ryusou/articles/nuxt-chartjs
// import { Line, mixins } from 'vue-chartjs'
import { Line } from 'vue-chartjs'
// const { reactiveProp } = mixins

export default {
  extends: Line,
  // mixins: [reactiveProp],
  props: {
    info: {
      type: Object
    },
    // chartData: {
    //   type: Object,
    //   default: null
    // },
    // options: {
    //   type: Object,
    //   default: null
    // }
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
        chartData:'',
        options:'',
    }
  },
  created() {
    // this.$store.dispatch('getHello')
    // this.getHello()
    // this.info = this.$store.state.info; // store/index.jsのstate.statusを取得
    console.log(this.info)

    this.contents = this.$store.state.contents;
    console.log(this.contents)

// 用
    this.createChart()

  },
  mounted() {
    this.renderChart(this.chartData, this.options)
  },
  methods: {
    
    createChart(){
      // https://qiita.com/kd9951/items/aece80abe0bd42b3b5d3
      this.chartData = {
        labels: this.priceDiaryDate(),
        // labels: ['2021/08/12','2021/08/13'],
        datasets: [
          {
            label: "始値",
            backgroundColor: 'rgb(232, 234, 246, 0.1)',
            borderColor: "#0000BB",
            yAxisID: "y_axis1",
            data: this.openPrice(),
            fill: false
          },
          {
            label: "終値",
            backgroundColor: 'rgb(232, 234, 246, 0.1)',
            borderColor: "#BB0000",
            yAxisID: "y_axis1",
            data: this.closePrice(),
            fill: false
          },
          {
            label: "高値",
            backgroundColor: 'rgb(232, 234, 246, 0.1)',
            borderColor: "#005500",
            yAxisID: "y_axis1",
            data: this.highPrice(),
            fill: false
          },
          {
            label: "安値",
            backgroundColor: 'rgb(232, 234, 246, 0.1)',
            borderColor: "#005500",
            yAxisID: "y_axis1",
            data: this.lowPrice(),
            fill: false
          },
          {
            type: 'bar', 
            label: "信用買残",
            backgroundColor: '#CCCCCC',
            borderColor: "#C5CAE9",
            yAxisID: "y_axis2",
            data: this.prchsMargin(),
            fill: false
          },
          {
            type: 'bar', 
            label: "信用売残",
            backgroundColor: '#FFFFBB',
            borderColor: "#C5CAE9",
            yAxisID: "y_axis2",
            data: this.salesMargin(),
            fill: false
          },
          {
            type: 'bar', 
            label: "信用倍率",
            backgroundColor: 'rgb(232, 234, 246, 0.1)',
            borderColor: "#C5CAE9",
            yAxisID: "y_axis2",
            data: this.ratioOfMargin(),
            fill: false
          },
        ]
      }
      this.options = {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          yAxes: [{
            id:"y_axis1",
            // stacked: true,
            stacked: false,
            ticks: {
              color: "#E8EAF6",
            },
            grid: {
              color: "rgb(232, 234, 246, 0.1)"
            },
          },
          {
            id:"y_axis2",
            position: "right",
            // stacked: true,
            stacked: false,
            ticks: {
              color: "#E8EAF6",
            },
            grid: {
              color: "rgb(232, 234, 246, 0.1)"
            },
          }],
          xAxes: {
            ticks: {
              color: "#E8EAF6",
            },
            grid: {
              color: "rgb(232, 234, 246, 0.1)"
            }
          }
        }
      }
    },
    
    priceDiaryDate(){
      const date = this.info.priceDiary.map(element => element[0])
      // console.log(date)
      return date
    },
    // priceDiaryTime(){
    //   const time = this.info.priceDiary.map(element => element[0])
    //   console.log(time)
    //   return time
    // },
    openPrice(){
      const openPrice = this.info.priceDiary.map(element => element[1])
      // console.log(openPrice)
      return openPrice
    },
    closePrice(){
      const closePrice = this.info.priceDiary.map(element => element[2])
      // console.log(closePrice)
      return closePrice
    },
    highPrice(){
      const highPrice = this.info.priceDiary.map(element => element[3])
      // console.log(highPrice)
      return highPrice
    },
    lowPrice(){
      const lowPrice = this.info.priceDiary.map(element => element[4])
      // console.log(lowPrice)
      return lowPrice
    },
    prchsMargin(){
      const prchsMargin = this.info.priceDiary.map(element => element[5])
      // console.log(prchsMargin)
      return prchsMargin
    },
    salesMargin(){
      const salesMargin = this.info.priceDiary.map(element => element[6])
      // console.log(salesMargin)
      return salesMargin
    },
    ratioOfMargin(){
      const ratioOfMargin = this.info.priceDiary.map(element => element[7])
      // console.log(ratioOfMargin)
      return ratioOfMargin
    },
  }
}
</script>