<template>




          <div class="form-wrapper">
            <div class="header">
              login
            </div>
            <div >
              <video id="videoCamera" :width="videoWidth" :height="videoHeight" autoplay></video>
              <canvas style="display:none;" id="canvasCamera" :width="videoWidth" :height="videoHeight" ></canvas>
            </div>
            <div class="input-wrapper">
              <div class="border-wrapper">
                <input type="text" name="username" v-model="user" placeholder="username" class="border-item" autocomplete="off">
              </div>
              <div class="border-wrapper">
                <input type="text" @keyup.enter="setImage()" name="password" v-model="pass" placeholder="password" class="border-item" autocomplete="off">
              </div>
            </div>
            <div class="action">
              <div class="btn" @click="setImage()">
                {{ loginText }}
              </div>
            </div>

          </div>

</template>
<script>
import axios from "axios";
import {ElMessage} from "element-plus";
export default {
  data () {
    return {
      videoWidth: 300,
      videoHeight: 300,
      imgSrc: '',
      thisCancas: null,
      thisContext: null,
      thisVideo: null,
      loginText:'登录',
      user:'hjh',
      pass:''
    }
  },
  mounted() {
    this.getCompetence()
  },
  methods: {
// 调用权限（打开摄像头功能）
    getCompetence () {
      var _this = this
      this.thisCancas = document.getElementById('canvasCamera')
      this.thisContext = this.thisCancas.getContext('2d')
      this.thisVideo = document.getElementById('videoCamera')
      // 旧版本浏览器可能根本不支持mediaDevices，我们首先设置一个空对象
      if (navigator.mediaDevices === undefined) {
        navigator.mediaDevices = {}
      }
      // 一些浏览器实现了部分mediaDevices，我们不能只分配一个对象
      // 使用getUserMedia，因为它会覆盖现有的属性。
      // 这里，如果缺少getUserMedia属性，就添加它。
      if (navigator.mediaDevices.getUserMedia === undefined) {
        navigator.mediaDevices.getUserMedia = function (constraints) {
          // 首先获取现存的getUserMedia(如果存在)
          var getUserMedia = navigator.webkitGetUserMedia || navigator.mozGetUserMedia || navigator.getUserMedia
          // 有些浏览器不支持，会返回错误信息
          // 保持接口一致
          if (!getUserMedia) {
            return Promise.reject(new Error('getUserMedia is not implemented in this browser'))
          }
          // 否则，使用Promise将调用包装到旧的navigator.getUserMedia
          return new Promise(function (resolve, reject) {
            getUserMedia.call(navigator, constraints, resolve, reject)
          })
        }
      }
      var constraints = { audio: false, video: { width: this.videoWidth, height: this.videoHeight, transform: 'scaleX(-1)' } }
      navigator.mediaDevices.getUserMedia(constraints).then(function (stream) {
        // 旧的浏览器可能没有srcObject
        if ('srcObject' in _this.thisVideo) {
          _this.thisVideo.srcObject = stream
        } else {
          // 避免在新的浏览器中使用它，因为它正在被弃用。
          _this.thisVideo.src = window.URL.createObjectURL(stream)
        }
        _this.thisVideo.onloadedmetadata = function (e) {
          _this.thisVideo.play()
        }
      }).catch(err => {
        console.log(err)
      })
    },
//  绘制图片（拍照功能）
    setImage () {

      // var _this = this
      // 点击，canvas画图
      this.thisContext.drawImage(this.thisVideo, 0, 0, this.videoWidth, this.videoHeight)
      // 获取图片base64链接
      this.getcomparisonresult(this.thisCancas.toDataURL('image/png'))

    },

    dataURItoBlob (dataURI) {
      // base64 解码
      let byteString = window.atob(dataURI.split(',')[1])
      let mimeString = dataURI.split(',')[0].split(':')[1].split(';')[0]
      let ab = new ArrayBuffer(byteString.length)
      let ia = new Uint8Array(ab)
      for (let i = 0; i < byteString.length; i++) {
        ia[i] = byteString.charCodeAt(i)
      }
      return new Blob([ab], {type: mimeString})
    },
    getcomparisonresult(data) {
      if( this.user==='hjh'&&this.pass==='hjh'){
        sessionStorage.setItem('ifLogin',true)
        ElMessage({
          message: '登陆成功!',
          type: 'success'
        })
        window.location.href='/stu'

      }
      let imgData = this.dataURItoBlob(data)
      var formdata = new FormData()
      formdata.append('imgData', imgData)
      let headers = {
        'Content-Type': 'multipart/form-data'
      }
      axios.post(
          // "http://hjh.nat300.top/validate", formdata,{headers: headers}
          "http://127.0.0.1:5000/validate", formdata,{headers: headers}
      ).then(res=>{
        console.log(res.data)

        if(res.data==='True'){
          sessionStorage.setItem('ifLogin',true)
          ElMessage({
            message: '登陆成功!',
            type: 'success'
          })
          window.location.href='/stu'
          // this.$router.push('/stu')
          // this.$router.go(1)

        }
        else {
          ElMessage({
            message: '请尽快找系统管理员录入人脸!',
            type: 'warning'
          })
        }
      })
    },
// 关闭摄像头

    stopNavigator () {
      this.thisVideo.srcObject.getTracks()[0].stop()
    }
  },

}

</script>
<style scoped>






body {
  display: flex;
  align-items: center;
  justify-content: center;
  /* background-color: #0e92b3; */
  background: url('../assets/img_5.png') no-repeat;
  background-size: 100% 100%;
}

.form-wrapper {
  width: 100%;
  height: 1000px;
  background-color: rgba(41, 45, 62, .8);
  color: #fff;
  border-radius: 2px;
  padding: 50px;
}

.form-wrapper .header {
  text-align: center;
  font-size: 35px;
  text-transform: uppercase;
  line-height: 100px;
}

.form-wrapper .input-wrapper input {
  background-color: rgb(41, 45, 62);
  border: 0;
  width: 100%;
  text-align: center;
  font-size: 15px;
  color: #fff;
  outline: none;
}

.form-wrapper .input-wrapper input::placeholder {
  text-transform: uppercase;
}

.form-wrapper .input-wrapper .border-wrapper {
  background-image: linear-gradient(to right, #e8198b, #0eb4dd);
  width: 100%;
  height: 50px;
  margin-bottom: 20px;
  border-radius: 30px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.form-wrapper .input-wrapper .border-wrapper .border-item {
  height: calc(100% - 4px);
  width: calc(100% - 4px);
  border-radius: 30px;
}

.form-wrapper .action {
  display: flex;
  justify-content: center;
}

.form-wrapper .action .btn {
  width: 60%;
  text-transform: uppercase;
  border: 2px solid #0e92b3;
  text-align: center;
  line-height: 50px;
  border-radius: 30px;
  cursor: pointer;
}

.form-wrapper .action .btn:hover {
  background-image: linear-gradient(120deg, #84fab0 0%, #8fd3f4 100%);
}

.form-wrapper .icon-wrapper {
  text-align: center;
  width: 60%;
  margin: 0 auto;
  margin-top: 20px;
  border-top: 1px dashed rgb(146, 146, 146);
  padding: 20px;
}

.form-wrapper .icon-wrapper i {
  font-size: 20px;
  color: rgb(187, 187, 187);
  cursor: pointer;
  border: 1px solid #fff;
  padding: 5px;
  border-radius: 20px;
}

.form-wrapper .icon-wrapper i:hover {
  background-color: #0e92b3;
}
</style>