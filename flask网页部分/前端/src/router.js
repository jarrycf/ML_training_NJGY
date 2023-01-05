import {createRouter,createWebHistory} from "vue-router";
import STU from './components/STU.vue'
import HOME from './components/HOME.vue'
import MEDICAL from './components/MEDICAL.vue'
import LOGIN from './components/Login.vue'
const router=createRouter({
    history:createWebHistory(),
    routes:[
        {path:"/",component:LOGIN},
        {path:'/stu',component:STU},
        {path:'/home',component:HOME},
        {path:'/medical',component:MEDICAL},
    ]
})

export default router