




<template>

  <div class="common-layout">
    <el-container v-if="ifShow">
      <el-header >

        <el-menu
            class="el-menu-demo"
            mode="horizontal"
        >
          <el-menu-item index="1" style="font-size: 30px;font-weight:bold;font-family: 楷体;padding: 0">Machine Learning Training </el-menu-item>
          <el-sub-menu index="2">
            <template #title>成员</template>
            <el-menu-item @click="showInfo(0)">胡靖浩</el-menu-item>
            <el-menu-item @click="showInfo(5)">黄荣添</el-menu-item>
            <el-menu-item @click="showInfo(2)">沈超凡</el-menu-item>
            <el-menu-item @click="showInfo(7)">张宇帆</el-menu-item>
            <el-menu-item @click="showInfo(4)">孙政邦</el-menu-item>
            <el-menu-item @click="showInfo(3)">姚俊</el-menu-item>
            <el-menu-item @click="showInfo(1)">马金辉</el-menu-item>
            <el-menu-item @click="showInfo(6)">吴京城</el-menu-item>

          </el-sub-menu>
          <el-menu-item index="4">
            <a href="https://github.com/jarrycf/ML-training" target="_blank">前往GitHub</a>
          </el-menu-item>
          <el-menu-item @click="saoMa">
            扫码赞助我们
          </el-menu-item>
        </el-menu>
      </el-header>
      <el-container >
        <el-aside width="200px">

          <el-scrollbar style="background:#ecf5ff">
              <el-menu
                  background-color="#ecf5ff"
                  class="el-menu-demo"
                  mode="vertical"
              >
                <el-menu-item
                    class="item2"
                >
                  Ai Select
                </el-menu-item>
                <el-menu-item
                    class="item"
                >
                  <router-link  to="/stu" class="router">学生群体划分</router-link>
                </el-menu-item>
                <el-menu-item
                    class="item">
                  <router-link to="/home"  class="router">房屋价格预测</router-link>
                </el-menu-item>
                <el-menu-item
                    class="item">
                  <router-link to="/medical"  class="router">癌症复发诊断</router-link>

                </el-menu-item>

                <el-menu-item v-for="i in [1,2,3,4,5,6,7,8]" class="item router">待出租(租金:{{i*1000}})</el-menu-item>
              </el-menu>

          </el-scrollbar>

        </el-aside>
        <el-main >
          <router-view></router-view>
        </el-main>
      </el-container>
      <el-footer style="background-color: #ecf5ff">
        <p>奇异市龙神区四号街小卖部 Tel：594594123 / 12345678（怪奇先生）e-mail：ls@bird.com</p>
      </el-footer>
    </el-container>
    <el-container v-else>
      <Login></Login>
    </el-container>
  </div>
    <el-dialog
        style="background-color:#ecf5ff;"
        v-for="item in data"
        v-model="item.vis"
        :title="item.name"
        width="40%"
    >
<!--            <el-aside width="350px">-->
<!--              <el-image :src="item.img" style="width: 300px; height: 300px"/>-->

<!--            </el-aside>-->
              <p style="font-size: 20px;line-height:35px;letter-spacing: 10px; color: #c2a2d2">{{item.info}}</p>

    </el-dialog>
    <el-dialog
        style="background-color:#ecf5ff"
        v-model="visMa"
        title="扫码赞助我们"
        width="40%"
    >
        <div class="common-layout">
              <el-image src="src/assets/img_4.png" />
        </div>

    </el-dialog>
</template>

<script>
import Login from "./components/Login.vue";
export default {
  name:'APP',
  components:{
    Login
  },
  data(){
    return {
      info:{
        hjh:'软件工程师的职责包括：\n' +
            '\n' +
            '设计和开发软件系统，并确保它们能够满足用户需求和业务要求\n' +
            '分析用户需求和业务流程，并设计出合理的软件结构\n' +
            '编写高质量的代码，并进行单元测试和集成测试\n' +
            '解决软件开发过程中遇到的技术问题\n' +
            '对软件系统进行维护和升级，以提高其稳定性和可用性\n' +
            '与其他开发人员、测试人员和产品经理等团队成员进行沟通协作，共同完成项目\n',
        mjh:'正在学习中....',
        scf:'正在学习中....',
        szb:'正在学习中....',
        hrt:'正在学习中....',
        yj:'正在学习中....',
        zyf:'正在学习中....',
        wjc:'正在学习中....',
      },
      ifLogin:false,
      visMa:false,
      data:[

      ]
    }
  },
  mounted() {
    this.data=[
      {vis:false,info:this.info.hjh,name:'智能2111-胡靖浩',img:'src/assets/img.png'},
      {vis:false,info:this.info.mjh,name:'智能2111-马金辉',img:'src/assets/img.png'},
      {vis:false,info:this.info.scf,name:'智能2111-沈超凡',img:'src/assets/img.png'},
      {vis:false ,info:this.info.yj ,name:'智能2111-姚俊',img:'src/assets/img.png' },
      {vis:false,info:this.info.szb,name:'智能2111-孙政邦',img:'src/assets/img.png'},
      {vis:false,info:this.info.hrt,name:'智能2111-黄荣添',img:'src/assets/img.png'},
      {vis:false,info:this.info.wjc,name:'智能2111-吴京城',img:'src/assets/img.png'},
      {vis:false,info:this.info.zyf,name:'智能2111-张宇帆',img:'src/assets/img.png'},
    ]
  },
  methods:{

    saoMa(){
      this.visMa=true
    },
    showInfo(index){
      this.data[index].vis=true
    }
  },
  computed:{
    ifShow(){
      console.log(window.location.href.split('/').pop())
      return window.location.href.split('/').pop()
    },
  }

}
</script>

<style scoped>


.item:hover{
  background-color: #c2a2d2;
}
.router{
  color: #537ae0;
  font-size: 20px;
  font-family: 楷体;
}
.item2{
  color: #537ae0;

  font-size: 30px;
  font-weight: bold;
  font-family: 隶书;

}

.flex-grow {
  flex-grow: 1;
}
.scrollbar-demo-item {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 50px;
  margin: 10px;
  text-align: center;
  border-radius: 4px;
  background: var(--el-color-primary-light-9);
  color: var(--el-color-primary);
}
</style>