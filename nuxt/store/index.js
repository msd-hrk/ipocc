// import axios from 'axios'

// https://arrown-blog.com/vuex-state-reset/
const getDefaultState = () => {
  return {
    info:'',
    // theme:'',
  }
}
// // ステート => アプリケーション全体の状態を保持するオブジェクト
export const state = () => getDefaultState()

// // ゲッター => ステートから別の値を算出するため用いる
export const getters = {
  // items: (state) => state.items
  // watchCounter: (state) => state.watchCounter
}

// // ミューテーション => ステートを更新するために用いる
export const mutations = {
  setHello(state, info){
    state.info = info;
    // console.log(info)
  },

  // リロード対応
  reload(state) {
    // console.log("session",sessionStorage.getItem('storeValues'))
    if(sessionStorage.getItem('storeValues') != null) { // 通常リンクによるレンダリングの場合を除くため。
      // const storeValues = JSON.parse(sessionStorage.getItem('storeValues')); // sessionStorageをjson形式にパース

      // state.theme = storeValues.theme;
      // state.firstFlag = storeValues.firstFlag
      // state.newHint = storeValues.newHint
      // state.hints = storeValues.hints
      // state.answers = storeValues.answers
      // state.newAnswer = storeValues.newAnswer
      // state.correct = storeValues.correct
    }
  },
}

// アクション => 非同期処理や外部APIとの通信を行い、最終的にミューテーションを呼び出すために用いる
export const actions = {
  // https://noumisoblog.com/vuex-persistedstate-nuxt/
  // nuxtClientInit({ commit }, context) { // クライアント側で初期化処理時に発火
  //   console.log("nuxtClientInit");
  //   commit('reload') // mutationのreloadメソッドを実行
  // },
  
  // https://github.com/TNK-2/flask-nuxt-docker/blob/master/front/store/index.js
  async getHello({commit}, state){
    // const info = ''
    const info = 
    await 
    this.$axios
    .$get("/hello")
    // .$get("/json")
    // .$get("http://localhost:3001/hello")
    // .then((response) => {
    //   (this.info = response)
    //   console.log(response)
    // }) // 変数infoに戻り値のjsonを格納
    // .catch((error) => { // エラー処理
    //   console.log(error);
    //   this.errored = true;
    // });

    console.log('getHello:',info);
        
    // console.log('$config:',$config);
    commit('setHello', info)
  },
}