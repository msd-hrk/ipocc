<template>
  <div>
    <!-- <Logo /> -->
    <h1>
      info.priceDiary
    </h1>
    {{ info.priceDiary }}
    <h1>
      info
    </h1>
    {{ info }}
    <!-- <h1>
      ipocc
    </h1>
    {{ ipocc }} -->
    <h1>
      jsonファイルを表示
    </h1>
    {{ posts }}
  </div>
</template>

<script>
import axios from 'axios'
export default {
  // async asyncData () {
  //   // const ipocc = await axios.get('/ipocc/')
  //   const ipocc = await axios.get('http://localhost:3001/ipocc')
  //   console.log(ipocc)
  //   return {ipocc}
  // },

  // https://ja.nuxtjs.org/docs/2.x/features/data-fetching
  async asyncData({ store }) {
    await store.dispatch('getHello')
  },

  data () {
    return {
      posts: '',
      ipocc: [],
      info: '',
    }
  },
  created() {
    this.getHello()
    this.info = this.$store.state.info; // store/index.jsのstate.statusを取得
    console.log(this.info)
  },
  mounted () {
    axios
      .get('http://localhost:3001/posts')
      .then((response) => {
        this.posts = response.data
      })
      .catch((error) => {
        // eslint-disable-next-line no-console
        console.log('There is error:' + error.response)
      })
  },
  methods:{
    getHello(){
      this.$axios
        .$get("/hello")
        .then((response) => (this.info = response)) // 変数infoに戻り値のjsonを格納
        .catch((error) => { // エラー処理
          console.log(error);
          this.errored = true;
        });
    }
  }
}
</script>

<style>
</style>