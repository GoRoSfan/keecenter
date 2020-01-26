import Vue from 'vue'
import App from './App.vue'
import router from './router'

import MuseUI from 'muse-ui';
import 'muse-ui/dist/muse-ui.css';
import theme from 'muse-ui/lib/theme';

Vue.use(MuseUI.Grid);
Vue.use(MuseUI.Pagination);

theme.add('keecenter_theme', {
  primary: '#FFD300',
  secondary: '#FFAA00',
  text: {
    primary: '#FFE773',
    secondary: '#3914AF',
    alternate: '#6C8CD5',
  },
  background: {
    paper: '#311491',
    chip: '#7109AA',
    default: '#FFE773',
  },
}, 'light');

theme.use('keecenter_theme');

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
