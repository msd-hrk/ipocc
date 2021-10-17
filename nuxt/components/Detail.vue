<template>
  <div >
    <v-card>
      <v-card-title>会社名：{{content.company}}</v-card-title>
      <v-card-text>
        事業内容：{{content.business}}
      </v-card-text>

      <v-card-text>priceDiary</v-card-text>
      <!-- {{priceDiary()}} -->
      <v-data-table
        :headers="headers"
        :items="desserts"
        :items-per-page="5"
        class="elevation-1"
      ></v-data-table>
    </v-card>
    <br><br><br>
    <div>
      content→{{content}}
      <br><br><br><br>
      index→{{index}}
      <br><br><br><br>
      contents→{{contents}}
    </div>
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
        headers: [
          {
            text: 'Date',
            align: 'start',
            sortable: false,
            value: 'date',
            // value: 'name',
          },
          { text: '始値', value: 'open' },
          { text: '高値', value: 'high' },
          { text: '安値', value: 'low' },
          { text: '終値', value: 'close' },
          { text: '信用買残', value: 'prchsMargin' },
          { text: '信用売残', value: 'salesMargin' },
          { text: '信用倍率', value: 'ratioOfMargin' },
          // { text: '始値', value: 'calories' },
          // { text: '高値', value: 'fat' },
          // { text: '安値', value: 'carbs' },
          // { text: '終値', value: 'protein' },
          // { text: '信用買残', value: 'iron' },
          // { text: '信用売残', value: 'iron' },
          // { text: '信用倍率', value: 'iron' },
        ],
        desserts: this.priceDiary()
        // [
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
        //   },
        //   {
        //     name: 'Eclair',
        //     calories: 262,
        //     fat: 16.0,
        //     carbs: 23,
        //     protein: 6.0,
        //     iron: '7%',
        //   },
        //   {
        //     name: 'Cupcake',
        //     calories: 305,
        //     fat: 3.7,
        //     carbs: 67,
        //     protein: 4.3,
        //     iron: '8%',
        //   },
        //   {
        //     name: 'Gingerbread',
        //     calories: 356,
        //     fat: 16.0,
        //     carbs: 49,
        //     protein: 3.9,
        //     iron: '16%',
        //   },
        //   {
        //     name: 'Jelly bean',
        //     calories: 375,
        //     fat: 0.0,
        //     carbs: 94,
        //     protein: 0.0,
        //     iron: '0%',
        //   },
        //   {
        //     name: 'Lollipop',
        //     calories: 392,
        //     fat: 0.2,
        //     carbs: 98,
        //     protein: 0,
        //     iron: '2%',
        //   },
        //   {
        //     name: 'Honeycomb',
        //     calories: 408,
        //     fat: 3.2,
        //     carbs: 87,
        //     protein: 6.5,
        //     iron: '45%',
        //   },
        //   {
        //     name: 'Donut',
        //     calories: 452,
        //     fat: 25.0,
        //     carbs: 51,
        //     protein: 4.9,
        //     iron: '22%',
        //   },
        //   {
        //     name: 'KitKat',
        //     calories: 518,
        //     fat: 26.0,
        //     carbs: 65,
        //     protein: 7,
        //     iron: '6%',
        //   },
        // ],
    }
  },
  computed: {
    // dataKeys() {
    //   // console.log("dataKeys:",Object.keys(this.data))
    //   return Object.keys(this.data);
    // },
  },
  created(){
  },
  mounted(){
  },
  methods: {
    priceDiary(){
      // Object.keys(content).filter(function(k) { return content[k] ==  })[0];
      // Object.values(this.content.priceDiary)
      const priceDiary = []
        // ${Object.keys(this.content.priceDiary)[i]}: ${Object.values(this.content.priceDiary)[i]}
      // 旧pricdDiaryの場合
        console.log(Object.values(this.content.priceDiary))
        for(let i = 0; i< Object.keys(this.content.priceDiary).length; i++){
          const diaryData = {}
          diaryData.date= Object.values(this.content.priceDiary[i])[0]
          diaryData.open= Object.values(this.content.priceDiary[i])[1]
          diaryData.close= Object.values(this.content.priceDiary[i])[2]
          diaryData.high= Object.values(this.content.priceDiary[i])[3]
          diaryData.low= Object.values(this.content.priceDiary[i])[4]
          diaryData.prchsMargin= Object.values(this.content.priceDiary[i])[5]
          diaryData.salesMargin= Object.values(this.content.priceDiary[i])[6]
          diaryData.ratioOfMargin= Object.values(this.content.priceDiary[i])[7]
          priceDiary.push(diaryData)
          // console.log(`diaryData→${JSON.stringify(diaryData)}`)
        }

      // pricdDiary案2の場合
        // // console.log(`entries→${JSON.stringify(Object.entries(this.content.priceDiary2))}`)
        // console.log(Object.values(this.content.priceDiary2))
        // for(let i = 0; i< Object.keys(this.content.priceDiary2).length; i++){
        //   // console.log(`entries[1][i]→${JSON.stringify(Object.entries(this.content.priceDiary2[1])[i])}`)
        //   const diaryData = {}
        //   for(let j = 0; j< Object.keys(this.content.priceDiary2[i]).length; j++){
        //     // diaryData[`foo${[j]}`] = Object.values(this.content.priceDiary2[i])[j]
        //     diaryData[Object.keys(this.content.priceDiary2[i])[j]] = Object.values(this.content.priceDiary2[i])[j]
        //     // console.log(`diaryData→${JSON.stringify(diaryData)}`)
        //   }
        //   priceDiary.push(diaryData)
        //   // console.log(`diaryData→${JSON.stringify(diaryData)}`)
        // }

      console.log(`data→${JSON.stringify(priceDiary)}`)
      // console.log(JSON.parse(priceDiary))
      return priceDiary
    },
  }
};
</script>
