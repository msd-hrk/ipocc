<template>
  <!-- マウント->プロパティから呼び出す場合。 -->
  <div>
    {{info}}
  </div>
  <!-- メソッドから呼び出す場合。ボタンをクリックするとログにapiを叩いた結果が出力される -->
  <!-- <v-btn><button v-on:click="showMessage">ボタン</button></v-btn> -->
</template>
<script>
import axios from 'axios'

export default {
  name: "note",
  data() {
    return {
      info: null,
      loading: true,
      errored: false,
    };
  },
  methods: {
    // showMessage() {
    //   this.$axios
    //     .$get("/hello")
    //     .then((res) => {
    //       console.log(res);
    //     })
    //     .catch((error) => {
    //       console.log(error);
    //     });
    // },
  },
  mounted() {
    this.$axios
      .$get("/hello")
      .then((response) => (this.info = response)) // 変数infoに戻り値のjsonを格納
      .catch((error) => { // エラー処理
        console.log(error);
        this.errored = true;
      });
  },
};
</script>