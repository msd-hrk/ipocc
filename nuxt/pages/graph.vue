<template>
  <div>
    <div class="small">
      <!-- https://github.com/ehajri/vue-chartjs-financial/blob/master/src/views/Candlestick.vue -->
      <h1>OHLC</h1>
      <Candlestick :chart-data="datacollection" :options="options" />
    </div>
    <br>
    <div class="chart-container">
      <h1>chart</h1>
      <chart
        :chartData="chartData"
        :options="options"
      />
    </div>

    <!-- <p>
      info.priceDiary
      <br>
      {{info.priceDiary}}
    </p>
    <br>
    {{info}} -->
  </div>
</template>
<script>
import chart from '../components/Chart'
import Candlestick from '@/components/Candlestick.js';

export default {
  components: { 
    chart,
    Candlestick,
  },

  // https://ja.nuxtjs.org/docs/2.x/features/data-fetching
  async asyncData({ store }) {
    await store.dispatch('getHello')
    await store.dispatch('getListedList')
  },

  data () {
    return{
      info:{},// helloで取得
      contents:[], // getListedListで取得(複数会社)
      content:{}, // getListedList？で取得(単独会社)

      datacollection: {}, // Candlestickに渡すデータ
      options: {}, // Candlestickでの表示option
    }
  },
  created(){
    // this.$store.dispatch('getHello')
    // this.getHello()
    this.info = this.$store.state.info; // store/index.jsのstate.statusを取得
    console.log(this.info)

    this.contents = this.$store.state.contents;
    console.log(this.contents)

// 確認用
    this.priceDiaryDate()
    this.priceDiaryAmt()
    // this.priceDiaryLabel()
// 確認用
    this.createChart()
  },
  mounted(){
    this.fillData();
    console.log("generateData:", this.generateData())
    console.log("datacollection:", this.datacollection)
  },
  methods:{
    fillData() {
      this.datacollection = {
        datasets: [
          {
            label: 'OHLC',
            // data: this.generateRandomData(),
            data: this.generateData(),
          },
        ],
      };
      this.options = {
        responsive: true,
        maintainAspectRatio: false,
        // https://r17n.page/2020/09/27/chartjs-tooltip-text-customize/
        tooltips: {
          callbacks: {
            // title: (tooltipItem, data) => {
            //   return `My Title`;
            // },
            label: (tooltipItem, data) => {
              // console.log(`tooltipItem:${Object.entries(tooltipItem)}`)
              // console.log(`tooltipItem.index:${tooltipItem.index}`)
              // console.log(`data:${Object.entries(data)}`)
              // return `${tooltipItem.value}, openPrice:${this.openPrice()}`;
              return [ // 項目ごとに改行する場合、string型の配列を戻り値にする。(配列の要素ごとに改行される)
                // https://stackoverflow.com/questions/29302392/chartjs-tooltip-line-breaks
                `o:￥${this.openPrice()[tooltipItem.index]}`,
                `h:￥${this.highPrice()[tooltipItem.index]}`,
                `l:￥${this.lowPrice()[tooltipItem.index]}`,
                `c:￥${this.closePrice()[tooltipItem.index]}`,
                `信用買残:${this.prchsMargin()[tooltipItem.index]}`,
                `信用売残:${this.salesMargin()[tooltipItem.index]}`,
                `信用倍率:${this.ratioOfMargin()[tooltipItem.index]}`,
              ];
            },
          },
          backgroundColor: 'black',
          borderColor: '#000',
          borderWidth: 3,
          displayColors: false,
          titleFontColor: 'grey',
          bodyFontColor: 'white',
        },
        scales: {
          yAxes: [{
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
    generateData(){
      const OHLCdata = []
      for(let i=0; i<=this.priceDiaryDate().length; i++) {  
        OHLCdata.push({ o: this.openPrice()[i],      // 始値
                        h: this.highPrice()[i],      // 高値
                        c: this.closePrice()[i],     // 終値
                        l: this.lowPrice()[i],       // 安値
                        t: this.priceDiaryDate()[i], // time
                      })
      }
      return OHLCdata
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
    priceDiaryAmt(){
      const firstAmount = this.info.priceDiary.map(element => element[1])
      // console.log(firstAmount)
      return firstAmount
    },
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
    createChart(){
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
    }
  }
}
</script>