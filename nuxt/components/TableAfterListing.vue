<template>
  <div >
    <h1>TableAfterListing.vue</h1>
    <v-card >
      <v-card-title>
        会社一覧(上場後の価格 TableAfterListing)
      <v-spacer></v-spacer>
        <v-text-field
          v-model="search"
          append-icon="mdi-magnify"
          label="Search"
          single-line
          hide-details
        ></v-text-field>
      </v-card-title>
      <v-data-table
        :headers="headers"
        :items="companylist"
        :items-per-page="8"
        :search="search"
        multi-sort
        :sort-by="['companyname', 'date1']"
        :sort-desc="[false, true]"
        class="elevation-1"
        color="green darken-1"
      ></v-data-table>
    </v-card>
    <!-- <br><br><br>
      <p>{{headers}}</p>
      <p>{{companylist}}</p>
    <div>
      content→{{content}}
      <br><br><br><br>
      index→{{index}}
      <br><br><br><br>
      contents→{{contents}}
    </div> -->
  </div>
</template>

<script>
export default {
  props: {
    content: {
      type: Object
    },
    index: {
      type: Number,
      default: 0
    },
    contents: {
      type: Object
    },
  },
  data(){
    return{
        Contents : Object.values(this.contents)[0],
        // headers: this.createHeaders(),
        search:'',
        headers: [],
        // [
        //   {
        //     text: '会社名',
        //     align: 'start',
        //     sortable: false,
        //     value: 'companyname',
        //     // value: 'name',
        //   },
        //   this.dateHeader()
          // { text: '上場初日', value: 'date1' },
          // { text: '上場2日目', value: 'date2' },
          // { text: '上場n日目', value: 'daten' },
          // // { text: '始値', value: 'open' },
          // // { text: '高値', value: 'high' },
          // // { text: '安値', value: 'low' },
          // { text: '終値', value: 'close' },
          // // { text: '信用買残', value: 'prchsMargin' },
          // // { text: '信用売残', value: 'salesMargin' },
          // // { text: '信用倍率', value: 'ratioOfMargin' },
        // ],
        // desserts: this.priceDiary(),
        // companylist: this.companyPriceDiary()
        
        // companylist: this.companyPriceDiary(),
        companylist: [],
        // [
          // {
          //   companyname: '会社a',
          //   date1:'上場初日のcloseの値',
          //   date2:'上場2日目のcloseの値',
          //   daten:'上場n日目のcloseの値',
          // },
          // {
          //   companyname: '会社b',
          //   date1:'上場初日のcloseの値',
          //   date2:'上場2日目のcloseの値',
          //   daten:'上場n日目のcloseの値',
          // }
        // desserts: [
        //   {
        //     name: 'Frozen Yogurt',
        //     calories: 159,
        //     fat: 6.0,
        //     carbs: 24,
        //     protein: 4.0,
        //     iron: '1%',
        //   },
        //   {
        //     name: 'Ice cream sandwich',
        //     calories: 237,
        //     fat: 9.0,
        //     carbs: 37,
        //     protein: 4.3,
        //     iron: '1%',
        //   }
        // ],
    }
  },
  computed: {
  },
  created(){
    // ヘッダー
    this.headers = this.createHeaders()

    // データ部
    this.companylist = this.priceRatioAfterListing() // priceDiary/公募価格
    // this.companylist = this.priceAfterListing() // priceDiary

    this.test = 1
  },
  mounted(){
  },
  methods: {
    createHeaders() {
      const headers = []
      headers[0] = {
                    text: '会社名',
                    align: 'start',
                    sortable: true,
                    value: 'companyname',
                    }
      headers[1] = {
                    text: '種類',
                    // align: 'start',
                    // sortable: false,
                    value: 'type',
                    }

      // priceDiaryの最大データ数の算出
      let priceDiaryLength = 0;
      // companyごとにループ
      // console.log(this.Contents.length)
      for(let i = 0; i< this.Contents.length ; i++){
        if(priceDiaryLength < this.Contents[i].priceDiary.length){
        // priceDiaryの最大データ数を格納
          priceDiaryLength = this.Contents[i].priceDiary.length;
        }
      }
      // console.log(priceDiaryLength)

      // ヘッダ(上場日数)の作成
      // priceDiaryをループ
      for(let j = 0; j< priceDiaryLength ; j++){
        const dateHeader = {}
        // dateHeader.text = `上場${j+1}日目`
        dateHeader.text = `${j+1}日目`
        dateHeader.value = `date${j+1}`
        headers.push(dateHeader)
        // console.log(`dateHeader:${JSON.stringify(dateHeader)}`)
      }
      // console.log(`headers:${JSON.stringify(headers)}`)
      return headers
    },
    
    // 上場後の価格割合(pricdDiary/公募価格)を算出、整形
    priceRatioAfterListing(){
      const priceRatioAfterListing = [] // 全社のpriceDiary情報
      // companyごとにループ
      for(let i = 0; i< this.Contents.length ; i++){
        const publicOfferingPrice = this.Contents[i].pubOfferPrice; // 公募価格
        // console.log(`publicOfferingPrice:${publicOfferingPrice}`)

        // 会社名
        // console.log('company:' + JSON.stringify(this.Contents[i].company))
        const openData = {} // 会社ごとの日次priceDiary(始値)
        const closeData = {} // 会社ごとの日次priceDiary(終値)
        openData.companyname = this.Contents[i].company;
        closeData.companyname = this.Contents[i].company;

        // 種類,データ部
        // console.log(this.Contents[i].priceDiary.length)
        const priceDiaryAll = this.Contents[i].priceDiary; // この会社のpriceDiary
        // priceDiaryをループ
        for(let j = 0; j< priceDiaryAll.length ; j++){
          let ratio;
          // console.log(`priceDiaryAll[${j}]:${priceDiaryAll[j]}`)
          
          // 始値
          openData.type = '始値(%)'
          ratio = (priceDiaryAll[j][1] / publicOfferingPrice) * 100
          openData[`date${j+1}`] = Math.round(ratio * 100)/100 // 小数点第2位で四捨五入

          // 終値
          closeData.type = '終値(%)'
          ratio = (priceDiaryAll[j][2] / publicOfferingPrice) * 100
          closeData[`date${j+1}`] = Math.round(ratio * 100)/100 // 小数点第2位で四捨五入
        }
        // console.log(`Data:${JSON.stringify(openData)}`)
        // console.log(`closeData:${JSON.stringify(closeData)}`)
        priceRatioAfterListing.push(openData, closeData)
      }
      return priceRatioAfterListing
        // [
          // {
          //   companyname: '会社a',
            // type: '終値',
          //   date1:'上場初日のcloseの割合',
          //   date2:'上場2日目のcloseの割合',
          //   daten:'上場n日目のcloseの割合',
          // },
        // ]
    },

    // 上場後の価格を整形
    priceAfterListing(){        
      const priceAfterListing = [] // 全社のpriceDiary情報
      // companyごとにループ
      for(let i = 0; i< this.Contents.length ; i++){
        // 会社名
        // console.log('company:' + JSON.stringify(this.Contents[i].company))
        const openData = {} // 会社ごとの日次priceDiary(始値)
        const closeData = {} // 会社ごとの日次priceDiary(終値)
        openData.companyname = this.Contents[i].company;
        closeData.companyname = this.Contents[i].company;

        // 種類,データ部
        // console.log(this.Contents[i].priceDiary.length)
        const priceDiaryAll = this.Contents[i].priceDiary; // この会社のpriceDiary
        // priceDiaryをループ
        for(let j = 0; j< priceDiaryAll.length ; j++){
          // console.log(`priceDiaryAll[${j}]:${priceDiaryAll[j]}`)
          
          // 始値
          openData.type = '始値'
          openData[`date${j+1}`] = priceDiaryAll[j][1]

          // 終値
          closeData.type = '終値'
          closeData[`date${j+1}`] = priceDiaryAll[j][2]
        }
        // console.log(`Data:${JSON.stringify(openData)}`)
        // console.log(`closeData:${JSON.stringify(closeData)}`)
        priceAfterListing.push(openData, closeData)
      }
      return priceAfterListing
        // [
          // {
          //   companyname: '会社a',
            // type: '終値',
          //   date1:'上場初日のcloseの値',
          //   date2:'上場2日目のcloseの値',
          //   daten:'上場n日目のcloseの値',
          // },
        // ]
    },
  }
};
</script>

<style scoped>
/* https://zenn.dev/gz/articles/e4c68d541ec054be905b */
.v-data-table--fixed-header >>> th:nth-child(1) {
    position: sticky !important;
    position: -webkit-sticky !important;
    left: 0;
    z-index: 9999;
    background: white;
}
</style>
