import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from './router'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import axios from "axios";

const app=createApp(App)
router.beforeEach(function (to,from ,next){
  if(to.path.length===1){
    next()
  }
  else if(sessionStorage.getItem('ifLogin')){
    next()
  }
  else {
    location.href='/'
  }


  // const sess=sessionStorage.getItem('ifLogin')
  // console.log(sess)
  // if(sess==null){
  //   next('/')
  // }else {
  //   next()
  //
  // }
})
app.use(router)
app.use(ElementPlus)

app.mount('#app')
