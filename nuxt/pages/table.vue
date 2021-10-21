<template>
  <div id="content">
    <table-after-listing
      :contents="contents"
      :content="content"
      :index=0
    >
    </table-after-listing>
    
    <Detail
      :contents="contents"
      :content="content"
      :index=0
    >
    </Detail>
    <br><br><br>
    <h1>VueJsonToTree</h1>
    <p>MongoDBみたいに、展開できる。</p>
    <!-- https://www.npmjs.com/package/vue-json-pretty -->
    <!-- <vue-json-pretty :path="'res'" :data="{ key: 'value' }" @click="handleClick"> </vue-json-pretty> -->
    <vue-json-pretty 
      :data="jsonDataArr"
      :deep="1"
      :showLength="true"
      :showLine="true"
      :showDoubleQuotes="false"
      :showSelectController="true"
    >
    </vue-json-pretty>

    <!-- <br><br><br>
    <h1>VueJsonToTable</h1>
    <p>テーブル表示。途中で断念...</p>
    <VueJsonToTableNew :data="jsonDataArr"/> -->
    <!-- <VueJsonToTable :data="jsonDataArr"/> -->
  </div>
</template>

<script>
import VueJsonPretty from 'vue-json-pretty';
import 'vue-json-pretty/lib/styles.css';
import Detail from '~/components/Detail.vue';
import TableAfterListing from '~/components/TableAfterListing.vue';

// import JsonToHtml from 'vue-json-to-html'
// import VueJsonToTable from 'vue-json-to-table'
// import VueJsonToTable from '../components/VueJsonToTable.vue'
// import VueJsonToTableNew from '../components/VueJsonToTableNew.vue'

export default {
  components: {
    VueJsonPretty,
    Detail,
    TableAfterListing,

    // JsonToHtml,
    // VueJsonToTable,
    // VueJsonToTableNew,
  },
  // https://ja.nuxtjs.org/docs/2.x/features/data-fetching
  // async asyncData({ store }) {
  //   await store.dispatch('getHello')
  // },
  
  // https://ja.nuxtjs.org/docs/2.x/features/data-fetching
  async asyncData({ store }) {
    await store.dispatch('getHello')
    await store.dispatch('getListedList')
  },

  data () {
    return{
      // json:''
      // jsonDataArr:''
      // jsonDataArr:{}
      jsonDataArr:jsonElements,
      // contents: contentsSample,
      contents: {},
      content: [],
    }
  },
  created(){
    console.log("created")
    // this.jsonDataArr = this.$store.state.info; // store/index.jsのstate.statusを取得
    // console.log(this.$store.state.info)

    this.contents = this.$store.state.contents;
    console.log(this.contents)

    this.content = Object.values(this.contents)[0][0]
      // content: Object.values(contentsSample)[0][0], // priceDiaryの変更テスト
      // content: Object.values(contentsSample)[0][i],
    console.log(this.content)
  },
}
export const jsonElements = 
        {
          // "InitPriceSellProfit": 2100, 
          // "absorbentAmount": {
          //   "beforePD": 7566720000
          // }, 
          // "bank": {
          //   "name": "みずほ証券", 
          //   "rate": "91.32％"
          // }, 
          // "bookbuilding": {
          //   "end": "20210716", 
          //   "start": "20210712"
          // }, 
          // "build": "2016", 
          // "business": "半導体パッケージ製造装置、有機ELパネル製造装置および液晶パネル製造装置などの開発・製造・販売およびアフターサービス", 
          // "capital": 450000000, 
          // "category": "機械", 
          // "cnsldtdFinInfo": [
          //   {
          //     "amountOfSalls": 14521324000, 
          //     "bps": 1194.59, 
          //     "eps": 51.76, 
          //     "fiscalYear": "202006", 
          //     "netIncome": 291396000, 
          //     "netWorth": 6727575000, 
          //     "ordinaryIncome": 396810000
          //   }, 
          //   {
          //     "amountOfSalls": 20261486000, 
          //     "bps": 1148.0, 
          //     "eps": 140.62, 
          //     "fiscalYear": "201906", 
          //     "netIncome": 791714000, 
          //     "netWorth": 6465425000, 
          //     "ordinaryIncome": 1257178000
          //   }
          // ], 
          // "company": "AIメカテック", 
          // "employee": {
          //   "age": 48, 
          //   "num": 202, 
          //   "salary": 685
          // }, 
          // "expectedProfitAfterTD": {
          //   "exProfit": {
          //     "max": 2000, 
          //     "min": -10000
          //   }, 
          //   "initPriceEx": {
          //     "max": 1940, 
          //     "min": 1820
          //   }, 
          //   "tdPrice": {
          //     "max": 1920, 
          //     "min": 1900
          //   }
          // }, 
          // "expectedProfitBeforeTD": {
          //   "exPrice": 1920, 
          //   "exProfit": {
          //     "max": 2000, 
          //     "min": -10000
          //   }, 
          //   "initPriceEx": {
          //     "max": 1940, 
          //     "min": 1820
          //   }
          // }, 
          // "grade": "Ｄ", 
          "holder_num": 2, 
          "indpndntFinInfo": [
            {
              "amountOfSalls": 14479693000, 
              "bps": 1167.15, 
              "dividend": 0.0, 
              "eps": 47.13, 
              "fiscalYear": "202006", 
              "netIncome": 265362000, 
              "netWorth": 6573077000, 
              "ordinaryIncome": 373535000
            }, 
            {
              "amountOfSalls": 20253519000, 
              "bps": 1120.02, 
              "dividend": 177.62, 
              "eps": 154.57, 
              "fiscalYear": "201906", 
              "netIncome": 870228000, 
              "netWorth": 6307865000, 
              "ordinaryIncome": 1254686000
            }, 
            {
              "amountOfSalls": 19449158000, 
              "bps": 57153.39, 
              "dividend": 0.0, 
              "eps": 7092.51, 
              "fiscalYear": "201806", 
              "netIncome": 763636000, 
              "netWorth": 6437636000, 
              "ordinaryIncome": 1074787000
            }
          ], 
          // "initPrice": 1941, 
          // "issuedShares": 5630000, 
          // "listingDate": "20210730", 
          // "market": "東証二部", 
          "mrktcptlz": {
            "beforePD": 10809600000
          }, 
          // "oaShared": 514000, 
          // "oar": 0.7, 
          // "pdd": "20210719", 
          "priceDiary": [
            [
              "20210730", 
              1941, 
              1707, 
              2043, 
              1676, 
              "---", 
              "---", 
              "---"
            ], 
            [
              "20210802", 
              1667, 
              1819, 
              1890, 
              1597, 
              "---", 
              "---", 
              "---"
            ], 
            [
              "20210803", 
              1739, 
              1800, 
              1845, 
              1720, 
              389100, 
              0, 
              0
            ], 
            [
              "20210804", 
              1782, 
              1742, 
              1805, 
              1659, 
              389100, 
              0, 
              0
            ], 
            [
              "20210805", 
              1710, 
              1728, 
              1766, 
              1669, 
              389100, 
              0, 
              0
            ], 
            [
              "20210806", 
              1700, 
              1817, 
              1818, 
              1696, 
              389100, 
              0, 
              0
            ]
          ], 
          // "pubOfferPrice": 1920, 
          // "pubOfferedShares": 0, 
          "purchasePeriod": {
            "end": "20210727", 
            "start": "20210720"
          }, 
          // "rfRate": 101.09, 
          // "securitiesNo": "6227", 
          // "sellShares": 3427000, 
          "shareholders": [
            {
              "lockup": {
                "day": 90, 
                "rate": 1.5, 
                "status": ""
              }, 
              "name": "ポラリス第三号投資事業有限責任組合", 
              "outShares": 2576900, 
              "position": "VC", 
              "potentialShares": 0, 
              "rate": "73.03％", 
              "sheredNum": 4233300
            }, 
            {
              "lockup": {
                "day": 90, 
                "rate": 1.5, 
                "status": ""
              }, 
              "name": "TiaraCGPrivateEquityFund2013,L.P.", 
              "outShares": 850100, 
              "position": "-", 
              "potentialShares": 0, 
              "rate": "24.09％", 
              "sheredNum": 1396700
            }, 
            {
              "lockup": {
                "day": 0, 
                "rate": 0, 
                "status": ""
              }, 
              "name": "阿部猪佐", 
              "outShares": 0, 
              "position": "代表取締役社長", 
              "potentialShares": 62700, 
              "rate": "1.08％", 
              "sheredNum": 62700
            }, 
            {
              "lockup": {
                "day": 0, 
                "rate": 0, 
                "status": ""
              }, 
              "name": "石田茂", 
              "outShares": 0, 
              "position": "取締役", 
              "potentialShares": 31350, 
              "rate": "0.54％", 
              "sheredNum": 31350
            }, 
            {
              "lockup": {
                "day": 0, 
                "rate": 0, 
                "status": ""
              }, 
              "name": "村上克宏", 
              "outShares": 0, 
              "position": "取締役", 
              "potentialShares": 31350, 
              "rate": "0.54％", 
              "sheredNum": 31350
            }, 
            {
              "lockup": {
                "day": 0, 
                "rate": 0, 
                "status": ""
              }, 
              "name": "小菅忠男", 
              "outShares": 0, 
              "position": "取締役", 
              "potentialShares": 13950, 
              "rate": "0.24％", 
              "sheredNum": 13950
            }, 
            {
              "lockup": {
                "day": 0, 
                "rate": 0, 
                "status": ""
              }, 
              "name": "土屋敬三", 
              "outShares": 0, 
              "position": "従業員", 
              "potentialShares": 13950, 
              "rate": "0.24％", 
              "sheredNum": 13950
            }, 
            {
              "lockup": {
                "day": 0, 
                "rate": 0, 
                "status": ""
              }, 
              "name": "野澤貞雄", 
              "outShares": 0, 
              "position": "従業員", 
              "potentialShares": 6950, 
              "rate": "0.12％", 
              "sheredNum": 6950
            }, 
            {
              "lockup": {
                "day": 0, 
                "rate": 0, 
                "status": ""
              }, 
              "name": "松浦康", 
              "outShares": 0, 
              "position": "取締役", 
              "potentialShares": 6950, 
              "rate": "0.12％", 
              "sheredNum": 6950
            }
          ], 
          "tdd": "20210708", 
          "unitShare": 100, 
          "web": "https://www.ai-mech.com/", 
          "winningNum": 39410
        }
</script>