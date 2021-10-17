// https://github.com/ehajri/vue-chartjs-financial/blob/master/src/components/Candlestick.js
// import { Candlestick, mixins } from 'vue-chartjs-financial';
import { Candlestick, mixins, Line, Bar} from 'vue-chartjs-financial';
const { reactiveProp } = mixins;

export default {
  // extends: Candlestick,
  extends: Candlestick, Line, Bar,
  // extends: [Candlestick, Line, Bar],
  mixins: [reactiveProp],
  props: ['options'],
  mounted() {
    this.renderChart(this.chartData, this.options);
  },
};