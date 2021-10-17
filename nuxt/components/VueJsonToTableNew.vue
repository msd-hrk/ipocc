// refer to: https://www.npmjs.com/package/vue-json-to-table
<template>
  <!-- <div class="table-main"> -->
  <div >
    <!-- <h1>data</h1>
    <p>{{data}}</p>
    <h1>previousData</h1>
    <p>{{previousData}}</p> -->
    
    <table border="1">
    <!-- <tr>
    <div
      v-for="(row, index) in dataKeys"
      :key="index"
    > -->
    <tr
      v-for="(dataKey, index) in dataKeys"
      :key="index"
    >
      <!-- <div class="key p-2 text-capitalize d-inline-block"> -->
      <!-- <div> -->
        <!-- <tr> -->
          <th>
          <!-- <p>hierarchy:{{hierarchy}}</p>
          <p>{{sameHeader(dataKey, index)}}</p> -->
          <th v-if="arrIndex===preArrIndex">
            <!-- arrindex:{{arrIndex}}
            preArrindex:{{preArrIndex}}
            header: -->
            {{ keyTitle(dataKey) }}
          </th>
          <!-- <th v-else v-show="showHeader"> -->
          <th v-else>
            <!-- arrindex:{{arrIndex}}
            preArrindex:{{preArrIndex}}
            header: -->
            {{ keyTitle(dataKey) }}
          </th>
        <!-- </tr> -->
      <!-- </div> -->
      <!-- <div v-if="['string', 'number'].includes(checkValueType(data[dataKey]))"> -->
      <td v-if="['string', 'number'].includes(checkValueType(data[dataKey]))">
        <!-- <div class="value p-2 d-inline-block">{{ data[dataKey] }}</div> -->
        <!-- <div>
          <tr>
            <td> -->
          <!-- data[dataKey]:  -->
          {{ data[dataKey] }}
            <!-- </td>
          </tr>
        </div> -->
      <!-- </div> -->
      </td>
      <!-- <div v-else-if="checkValueType(data[dataKey]) === 'array'"> -->
      <div v-else-if="checkValueType(data[dataKey]) === 'array'">
        <!-- <div v-if="!diffHeader"> -->
        <!-- <div v-for="(arrRow, index2) in data[dataKey]" :key="index2" class="d-flex"> -->
        <!-- <tr v-for="(arrRow, index2) in data[dataKey]" :key="index2" class="d-flex"> -->
        <tr v-for="(arrRow, index2) in data[dataKey]" :key="index2" class="d-flex">
          <!-- <div class="mx-2">--</div> -->
          <div>--</div>
          <!-- <div>--{{checkValueType(arrRow)}}</div> -->
          <!-- <div v-if="['string', 'number'].includes(checkValueType(arrRow))"> -->
          <td v-if="['string', 'number'].includes(checkValueType(arrRow))">
            <!-- <tr> -->
              <!-- <td> -->
            <!-- arrRow: -->
            {{ arrRow }}
              <!-- </td> -->
            <!-- </tr> -->
          <!-- </div> -->
          </td>
          <div v-else>
            <!-- <VueJsonToTable :data="arrRow" /> -->
            <VueJsonToTableNew
              :data="arrRow"
              :previousData="data[dataKey]"
              :hierarchy="hieNum"
              :arrIndex="index"
              :preArrIndex="arrCount"
            />
          </div>
        <!-- </div> -->
        </tr>
        <!-- </div> -->
      </div>
      <div v-else>
        <!-- <VueJsonToTable :data="data[dataKey]" /> -->
        <VueJsonToTableNew
          :data="data[dataKey]"
          :previousData="dataKeys"
          :hierarchy="hieNum"
        />
      </div>
    <!-- </div> -->
    </tr>
    </table>
  </div>
</template>

<script>
import VueJsonToTableNew from "./VueJsonToTableNew";
export default {
  name: 'VueJsonToTableNew',
  components: {
    VueJsonToTableNew
  },
  props: {
    data: {
      type: Object
    },
    // dataTypeの履歴を残すため
    dataType: {
      type: String,
      default: null
    },
    previousData: {
      type: Object,
      default: null
    },
    // jsonの階層管理
    hierarchy:{
      type: Number,
      default:0
    },
    // json内の配列index管理
    arrIndex:{
      type: Number,
      default:0
    },
    // json内の配列index管理
    preArrIndex:{
      type: Number,
      default:0
    }
  },
  data(){
    return{
      hieNum:this.hierarchy,
      arrNum:this.arrIndex,
      showHeader:true,
    }
  },
  computed: {
    dataKeys() {
      // console.log("dataKeys:",Object.keys(this.data))
      return Object.keys(this.data);
    },
    predataKeys() {
      // console.log("predataKeys:",Object.keys(this.previousData))
      return Object.keys(this.previousData);
    },
    arrCount() {
      return this.arrIndex + this.arrIndex + 1
    }
  },
  created(){
    this.hieNum = this.hierarchy + 1
    this.arrNum = this.arrIndex + 1
    console.log(`created hierarchy: ${this.hierarchy} hieNum: ${this.hieNum}`)
  },
  mounted(){
    // this.hieNum = this.hierarchy + 1
    console.log(`mounted hierarchy: ${this.hierarchy} hieNum: ${this.hieNum}`)
    // this.arrNum = this.arrIndex + 1
  },
  methods: {
    keyTitle(key) {
      // console.log("keyTitle(key):",key.split("_").join(" "))
      return key.split("_").join(" ");
    },
    checkValueType(val) {
      // console.log(`typeof val:${typeof val}`)
      if (typeof val !== "object") {
        return typeof val;
      }
      console.log(`isArray?:${Array.isArray(val)}`)
      // if (Array.isArray(val)) console.log(val)
      // if (Array.isArray(val)) console.log(val[0])
      // if (Array.isArray(val)) console.log(Object.keys(val[0]))
      return Array.isArray(val) ? "array" : "object";
    },
    sameHeader(dataKey, index, arrIndex){
      // console.log(`arrIndex:${this.arrIndex}`)

      if(this.previousData!==null && this.previousData!==undefined 
        && this.previousData[index]!==null && this.previousData[index]!==undefined
        && Array.isArray(this.previousData)){
        // console.log(`dataKeys:${Object.keys(this.data)}, predataKeys:${this.previousData}`)
        // console.log(`dataKeys:${Object.keys(this.data)}, predataKeys:${Object.keys(this.previousData[index])}, index:${index}`)
      // this.arrCount()
        // if(this.hieNum=== this.hierarchy){
        if(index>0){
        // console.log(dataKey, index)
        // if(this.previousData!==null && this.previousData!==undefined && typeof this.previousData === 'object'){
        //   if (JSON.stringify(Object.keys(this.data)) === JSON.stringify(Object.keys(this.previousData))){
          if (JSON.stringify(Object.keys(this.data)) === JSON.stringify(Object.keys(this.previousData[index]))){
        //     // console.log(`now:${Object.keys(this.data)} pre:${Object.keys(this.previousData)}`)
            // console.log(`now:${Object.keys(this.data)} pre:${Object.keys(this.previousData[index])}`)
            // console.log(`dataKey:${dataKey}`)
            // this.child_arrCount()
            this.showHeader=false
            console.log('一致！')
            return true
          }
        }
      }
      return false
    },
    // parent_arrCount(item){
    //   // this.arrNum = this.arrNum+1
    //   console.log('parent_arrCount', item)
    //   this.arrNum++
    //   // this.$emit('parent_arr-count', this.arrNum)
    // },
    // child_arrCount(){
    //   console.log('child_arrCount')
    //   this.$emit('parent_arrCount',this.$event)
    // },
    // parentEvent(item) {
    //   console.log('parentEvent',item)
    // },
    // childEvent() {
    //   this.arrNum++
    //   this.$emit('parent-event', this.arrNum)
    // }
    // arrCount(){
    //   return this.arrIndex + 1
    // },
    // calHierarchy(val){
    //   return val++
    // },
  }
};
</script>

<style lang="scss" scoped>
.m-2 {
  margin: .5rem!important;
}
.mx-2 {
  margin-right: .5rem!important;
}
.p-2 {
  padding: .5rem!important;
}
.d-flex {
  display: flex!important;
}
.d-inline-block {
  display: inline-block!important;
}
.text-capitalize {
  text-transform: capitalize!important;
}
.key {
  background: lightgray;
}
.table-main {
  .row-data {
    border: 2px solid grey;
    border-radius: 2px;
  }
}
</style>