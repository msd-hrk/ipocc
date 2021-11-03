<template>
  <div >
    <h1>TableAfterListing.vue</h1>
    <v-card >
      <v-card-title>
        会社一覧(上場後の価格 TableAfterListing)
        <v-spacer></v-spacer>
        <v-spacer></v-spacer>
        <v-select
          v-model="search"
          :items="types"
          label="単一種類の表示"
        ></v-select>
      </v-card-title>
        
      <v-card-subtitle>
        <v-text-field
          v-model="search"
          append-icon="mdi-magnify"
          label="Search"
          hide-details
        ></v-text-field>
      </v-card-subtitle>
      
      <!-- https://qiita.com/shin_ts/items/0dec5b2f97f90916a1a5 -->
      <v-data-table
        :headers="headers"
        :items="companylist"
        :items-per-page="8"
        :search="search"
        multi-sort
        :sort-by="['company', 'date1']"
        :sort-desc="[false, true]"
        fixed-header
        height="500"
        class="tableAfterListing"
      >

        <!-- 会社サイトへリンク https://www.paveway.info/entry/2020/12/11/vuetifyjs_vdatatablelink -->
        <!-- <template v-slot:[`item.web`]="{ item }"> -->
        <template v-slot:[`item.company`]="{ item }">
          <!-- <div v-if="!sameCompanyName(item.company)" -->
            <a v-if="item.web" target="_blank" :href="item.web">
              <!-- <div v-if="!sameCompanyName(item.company)" dark> -->

              {{ item.company }}
              <!-- </div> -->
            </a>
            <p v-else>{{ item.company }}</p>
          <!-- </div> -->
        </template>
        
        <!-- ツールチップ機能付きアイコン https://zenn.dev/katoaki/articles/a53d1dd254992b -->
        <!-- https://qiita.com/pokoTan2525/items/c698457d2473dab0868f -->
        <!-- <template v-slot:item.scheduledAt="{ item }"> -->
        <template v-slot:[`item.InitPriceSellProfit`]="{ item }">
          <v-tooltip v-if="item.InitPriceSellProfit" bottom >
            <template v-slot:activator="{ on, attrs }">
              <v-icon
                dark
                v-bind="attrs"
                v-on="on"
              >
                mdi-information-outline
              </v-icon>
            </template>
            <div>InitPriceSellProfit：{{ item.InitPriceSellProfit }}</div>
            <div v-if="item.capital">資本金：{{ item.capital }}</div>
            <div v-if="item.business">事業内容：{{ item.business }}</div>
            <div v-if="item.category">業種：{{ item.category }}</div>
            <div v-if="item.build">設立年度：{{ item.build }}</div>
            <div v-if="item.employee">~従業員情報~ 平均年齢?：{{ item.employee.age }}  社員数?：{{ item.employee.age }}  平均年収?：{{ item.employee.salary }}</div>
            <div v-if="item.grade">grade：{{ item.grade }}</div>
            <div v-if="item.initPrice">initPrice：{{ item.initPrice }}</div>
            <div v-if="item.securitiesNo">securitiesNo：{{ item.securitiesNo }}</div>
            <div v-if="item.pubOfferPrice">pubOfferPrice：{{ item.pubOfferPrice }}</div>
          </v-tooltip>
        </template>

        <!-- 色変換 -->
          <!-- templateタグ内でv-forを使う際の注意点 https://qiita.com/shizen-shin/items/ee97ace80f6945519c39 -->
          <!-- templateタグ内のv-for参考 https://jsfiddle.net/mysticatea/zuyjom9m/47/ -->
        <template v-for="i in counter" v-slot:[`item.date${i}`]="{ item }" >
          <v-chip
            :key="i"
            :color="getColor( item[`date${i}`] )"
            outlined
            dark
          >
            {{ item[`date${i}`] }}
          </v-chip>
        </template>
        <!-- <template v-for="i in counter" v-slot:[`item.date${i}`]="{ item }" >
          <v-chip
            :key="i"
            :color="getColor( getDateData(item, i).value )"
            dark
          >
            {{ getDateData(item, i).value }}
          </v-chip>
        </template> -->
        <!-- <template v-slot:[`item.date1`]="{ item }">
          <v-chip
            :color="getColor(item.date1)"
            dark
          >
            {{ item.date1 }}
          </v-chip>
        </template> -->
      </v-data-table>
      
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
        types:['', '始値', '終値'],
        headers: [],
        counter:'',
        preComapnyName:'',
        // [
        //   {
        //     text: '会社名',
        //     align: 'start',
        //     sortable: false,
        //     value: 'company',
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
          //   company: '会社a',
          //   date1:'上場初日のcloseの値',
          //   date2:'上場2日目のcloseの値',
          //   daten:'上場n日目のcloseの値',
          // },
          // {
          //   company: '会社b',
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
    sameCompanyName(nowCompanyName){
      let sameCompanyflag = false;
      if (this.preComapnyName === nowCompanyName) sameCompanyflag = true
      this.preComapnyName = nowCompanyName
      return sameCompanyflag
    },
    createHeaders() {
      const headers = []
         
      headers[0] = { text: 'info', value: 'InitPriceSellProfit',width: '30'  } // slotでカスタマイズするため、valueの指定は必須となる	
      headers[1] = {
                    text: '会社名',
                    align: 'start',
                    sortable: true,
                    value: 'company',
                    width: '150' ,
                    }
      headers[2] = {
                    text: '種類',
                    // align: 'start',
                    // sortable: false,
                    value: 'type',
                    width: '80' ,
                    }

      // priceDiaryの最大データ数の算出
      let priceDiaryLength = 0;
      // companyごとにループ
      // console.log(this.Contents.length)
      for(let i = 0; i< this.Contents.length ; i++){
        if(priceDiaryLength < this.Contents[i].priceDiary.length){
        // priceDiaryの最大データ数を格納
          priceDiaryLength = this.Contents[i].priceDiary.length;
          this.counter = priceDiaryLength
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

        // 会社情報get 
        this.getCompanyInfo(this.Contents[i], openData);
        this.getCompanyInfo(this.Contents[i], closeData);

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
          openData[`date${j+1}`] = Math.round(ratio * 100)/100 // 小数点第2位で四捨五入{JSON.stringify(closeData)}`)

          // 終値
          closeData.type = '終値(%)'
          ratio = (priceDiaryAll[j][2] / publicOfferingPrice) * 100
          closeData[`date${j+1}`] = Math.round(ratio * 100)/100 // 小数点第2位で四捨五入
        }
        // console.log(`Data:${JSON.stringify(openData)}`)
        // console.log(`closeData:$

        priceRatioAfterListing.push(openData, closeData)
      }
      return priceRatioAfterListing
        // [
          // {
          //   company: '会社a',
            // type: '終値',
          //   date1:'上場初日のcloseの割合',
          //   date2:'上場2日目のcloseの割合',
          //   daten:'上場n日目のcloseの割合',
          // },
        // ]
    },

    // 詳細情報付与 
    getCompanyInfo(companyInfo, data){
      // console.log("getCompanyInfo")
      // keys取得
      const companyInfoKeys = Object.keys(companyInfo)
      // console.log(`companyInfoKeys:${companyInfoKeys}`)
      // keyでループ
      companyInfoKeys.forEach(key => {
        // console.log(key)
        // value取得
        const companyInfoValue = companyInfo[key]
        // console.log(companyInfoValue)
        
        // valueの型判定 // https://qiita.com/amamamaou/items/ef0b797156b324bb4ef3
        const isPrototype = Object.prototype.toString.call(companyInfoValue).slice(8, -1).toLowerCase()
        // console.log(`${key} isPrototype:${isPrototype}`)

        // 型が"string" | "number"のとき
        if (isPrototype === "string" || isPrototype === "number"){
          data[key] = companyInfoValue // dataに付与
        }

        // keyが"employee"のとき
        if (key === "employee"){
          data[key] = companyInfoValue // dataに付与
          // console.log(`employee:${JSON.stringify(data[key])}`)
        }
      });
      // console.log(`data:${JSON.stringify(data)}`)
      return {data}
    },

    // 色分け準備 
    getDateData (item, i) {
      // const value = `item.date${i}`
      const value = item[`date${i}`]
      const text = "item.date"+i
      // console.log(`value:${value}, text:${text}`)
      // console.log(`getDateData ${i}:${JSON.stringify(item)}`)
      return {value, text}
    },
    // 色分け
    getColor (value) {
      if (value >= 200) return 'green'
      else if (value >= 100) return 'blue'
      else if (value >= 50) return 'orange'
      else if (value >= 0) return 'red'
      else return 'dark'
    },
    // // 上場後の価格を整形
    // priceAfterListing(){        
    //   const priceAfterListing = [] // 全社のpriceDiary情報
    //   // companyごとにループ
    //   for(let i = 0; i< this.Contents.length ; i++){
    //     // 会社名
    //     // console.log('company:' + JSON.stringify(this.Contents[i].company))
    //     const openData = {} // 会社ごとの日次priceDiary(始値)
    //     const closeData = {} // 会社ごとの日次priceDiary(終値)
    //     openData.company = this.Contents[i].company;
    //     closeData.company = this.Contents[i].company;

    //     // 種類,データ部
    //     // console.log(this.Contents[i].priceDiary.length)
    //     const priceDiaryAll = this.Contents[i].priceDiary; // この会社のpriceDiary
    //     // priceDiaryをループ
    //     for(let j = 0; j< priceDiaryAll.length ; j++){
    //       // console.log(`priceDiaryAll[${j}]:${priceDiaryAll[j]}`)
          
    //       // 始値
    //       openData.type = '始値'
    //       openData[`date${j+1}`] = priceDiaryAll[j][1]

    //       // 終値
    //       closeData.type = '終値'
    //       closeData[`date${j+1}`] = priceDiaryAll[j][2]
    //     }
    //     // console.log(`Data:${JSON.stringify(openData)}`)
    //     // console.log(`closeData:${JSON.stringify(closeData)}`)
    //     priceAfterListing.push(openData, closeData)
    //   }
    //   return priceAfterListing
    //     // [
    //       // {
    //       //   company: '会社a',
    //         // type: '終値',
    //       //   date1:'上場初日のcloseの値',
    //       //   date2:'上場2日目のcloseの値',
    //       //   daten:'上場n日目のcloseの値',
    //       // },
    //     // ]
    // },

  }
};
</script>

<style scoped>
/* v-data-tableの列固定 https://zenn.dev/gz/articles/e4c68d541ec054be905b */
/* 「>>>」Vue.jsでのdeep selectorの書き方 https://qiita.com/h-naito/items/f6ca679276282dce2600 */
/* 何番目系の便利なCSSまとめ https://qiita.com/ituki_b/items/62a752389385de7ba4a2 */
/* :nth-child():  https://developer.mozilla.org/ja/docs/Web/CSS/:nth-child */
/* CSSで使われる「#」「>」「$」などの意味とは？ https://kredo.jp/media/css-symbol-meaning/ */
/* nth-childとnth-of-typeでよく使う倍数や範囲の逆引き集 https://www.itti.jp/web-design/css-nth-child/ */
/* 「position: sticky」 https://coliss.com/articles/build-websites/operation/css/css-position-sticky-how-it-really-works.html */
/* z-indexとは https://jajaaan.co.jp/web-production/frontend/z-index/ */

/* .v-data-table--fixed-header >>> th:nth-child(1) { */
.v-data-table--fixed-header ::v-deep th:nth-child(n+1):nth-child(-n+2) {
    position: sticky !important;
    position: -webkit-sticky !important;
    left: 0;
    z-index: 9999;
    background: rgb(68, 15, 2);
}

/* .tableAfterListing /deep/ tbody > tr:nth-child(2n){ */
.tableAfterListing /deep/ tbody > tr:nth-child(n) > td:nth-child(n+1):nth-child(-n+2){
    position: sticky !important;
    position: -webkit-sticky !important;
    left: 0;
    z-index: 10;
    background: rgb(85, 0, 0);
}

</style>
