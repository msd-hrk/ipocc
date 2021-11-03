<template>
  <div style="margin: 50px">
    <p>{{ message }}</p>
    <h1>id：{{ this.$route.params.securitiesNo }}</h1>
  </div>
</template>

<script>
export default {
  data (){
    return {
      message:'/details/_securitiesNo.vueを表示中'
    }
  }
}
</script>