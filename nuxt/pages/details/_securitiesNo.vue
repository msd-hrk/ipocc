<template>
  <div style="margin: 50px">
    <p>{{ message }}</p>
    <h1>securitiesNo：{{ $route.params.securitiesNo }}</h1>
    <Detail
      :contents="securitiesNoData"
      :content="securitiesNoData"
      :index=0
    />

    <OHLC
      :contents="securitiesNoData"
      :info="securitiesNoData"
    />
    <div>
      <h1>MixedChart</h1>
      <MixedChart
        :info="securitiesNoData"
      />
    </div>

    <h1>VueJsonToTree</h1>
    <p>MongoDBみたいに、展開できる</p>
    <!-- https://www.npmjs.com/package/vue-json-pretty -->
    <!-- <vue-json-pretty :path="'res'" :data="{ key: 'value' }" @click="handleClick"> </vue-json-pretty> -->
    <vue-json-pretty 
      :data="securitiesNoData"
      :deep="1"
      :showLength="true"
      :showLine="true"
      :showDoubleQuotes="false"
      :showSelectController="true"
    >
    </vue-json-pretty>
    <p>{{ securitiesNoData }}</p>
  </div>
</template>

<script>
import Detail from '~/components/Detail.vue';
import OHLC from '~/components/OHLC.vue';
import MixedChart from '~/components/MixedChart.vue';

export default {
  components: {
    Detail,
    OHLC,
    MixedChart,
  },

  // https://ja.nuxtjs.org/docs/2.x/features/data-fetching
  async asyncData({ store }) {
    // await store.dispatch('getHello')
    await store.dispatch('getListedList')
  },
  data (){
    return {
      message:'/details/_securitiesNo.vueを表示中',
      
      // contents: {},
      // content: [],
      Contents : {},
      securitiesNoData: {},
      securitiesNo:'',
    }
  },
  created(){
    console.log("created")
    // this.jsonDataArr = this.$store.state.info; // store/index.jsのstate.statusを取得
    // console.log(this.$store.state.info)

    // this.contents = Object.values(this.$store.state.contents)[0];
    // console.log(this.contents)

    // this.content = Object.values(this.contents)[0][0]
    // console.log(this.content)

    this.Contents = Object.values(this.$store.state.contents)[0];
    // console.log(this.Contents)

    this.securitiesNoData = this.searchSecuritiesNoData(this.Contents)
  },
  mounted(){
  },
  methods: {
    searchSecuritiesNoData(Contents){
      // console.log(Contents);
      // console.log(this.$route.params.securitiesNo)
      let data = {}
      Contents.forEach(element => {
        console.log(element.securitiesNo)
        if(element.securitiesNo === this.$route.params.securitiesNo){
          console.log(`一致!${element.securitiesNo}`)
          data = element
        }
      });
      return data
    },
  }
}
</script>