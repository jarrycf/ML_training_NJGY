<template>
  <div class="flex">

    <el-upload
        drag
        class="upload-demo"
        action=""
        multiple
        :http-request="uploadFile"
    >
      <div class="el-upload__text">
        Drop file here or <em>click to upload</em>
      </div>
      <template #tip>
        <div class="el-upload__tip">
          csv/txt/excel files with a size less than 50000kb
        </div>
      </template>
    </el-upload>

  </div>
  <el-row>
    <el-col :span="6"><div class="grid-content ep-bg-purple" />
      <el-input
          v-model="sno" placeholder="Please input" @keyup.enter="searchEnter"/>
    </el-col>
    <el-col :span="4"><div class="grid-content ep-bg-purple-light" />
      <el-button type="primary" @click="searchEnter" >搜索房屋编号</el-button>

    </el-col>
    <el-col :span="2"><div class="grid-content ep-bg-purple-light" />
      <el-button type="primary" @click="addData" >新增数据</el-button>

    </el-col>
  </el-row>


  <el-table :data="data.slice((page-1)*pageSize,page*pageSize)" style="width: 100%">
    <el-table-column label="房屋编号" prop="id" />
    <el-table-column label="房屋年龄（单位：年）" prop="house_age" />
    <el-table-column label="离最近地铁站距离（单位：米）" prop="nearest_mrt" />
    <el-table-column label="生活圈便利店数量（单位：个）" prop="stores" />
    <el-table-column label="房屋价格（万元/坪）" prop="price_area" />


    <el-table-column align="right">
      <template #header>
        <el-button type="primary" @click="deleteAll">全部删除</el-button>

      </template>
      <template #default="scope">
        <el-button size="small" type="primary" @click="handleEdit(scope.row)"
        >Edit</el-button
        >
        <el-popconfirm
            confirm-button-text="OK"
            cancel-button-text="No"
            cancel-button-type="success"
            @confirm="handleDelete(scope.row.id)"
            title="Are you sure to delete this?"
        >
          <template #reference>
            <el-button
                size="small"
                type="danger"
            >Delete</el-button
            >
          </template>
        </el-popconfirm>

      </template>
    </el-table-column>
  </el-table>

  <div class="demo-pagination-block">
    <el-pagination
        v-model:current-page="currentPage4"
        v-model:page-size="pageSize4"
        :page-sizes="[10, 20, 30, 40]"
        :small="small"
        :disabled="disabled"
        :background="background"
        layout="total, sizes, prev, pager, next, jumper"
        :total="data.length"
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
    />
  </div>

  <el-dialog
      v-model="dialogVisible"
      title="房屋信息编辑"
      width="40%"
  >
    <template #footer>
      <el-form
          class="demo-ruleForm"
      >
<!--        <el-form-item label="&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp交易日期&nbsp" >-->
<!--          <el-date-picker-->
<!--              format="yyyy-MM-dd"-->
<!--              v-model="formData.transaction_date"-->
<!--              type="date"-->
<!--              placeholder="Pick a day"-->
<!--          />-->
<!--        </el-form-item>-->

        <el-form-item label="&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;房屋年龄（单位：年）" >
          <el-input  type="text" v-model="formData.house_age" autocomplete="off" />
        </el-form-item>


        <el-form-item label="离最近地铁站距离（单位：米）" >
          <el-input  type="text" v-model="formData.nearest_mrt" autocomplete="off" />
        </el-form-item>

        <el-form-item label="生活圈便利店数量（单位：个）" >
          <el-input  type="text" v-model="formData.stores" autocomplete="off" />
        </el-form-item>



        <el-form-item>
          <el-button style="margin: auto;width: 100px" type="primary" @click="submitForm()"
          >确定</el-button
          >
        </el-form-item>

      </el-form>

    </template>
  </el-dialog>

  <el-dialog
      v-model="dialogVisible2"
      title="房屋信息添加"
      width="40%"
  >
    <template #footer>
      <el-form
          class="demo-ruleForm"
      >
<!--        <el-form-item label="&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp交易日期&nbsp" >-->
<!--          <el-date-picker-->
<!--              format="yyyy-MM-dd"-->
<!--              v-model="formData2.transaction_date"-->
<!--              type="date"-->
<!--              placeholder="Pick a day"-->
<!--          />-->
<!--        </el-form-item>-->

        <el-form-item label="&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;房屋编号" >
          <el-input  type="text" v-model="formData2.id" autocomplete="off" />
        </el-form-item>

        <el-form-item label="&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;房屋年龄（单位：年）" >
          <el-input  type="text" v-model="formData2.house_age" autocomplete="off" />
        </el-form-item>


        <el-form-item label="离最近地铁站距离（单位：米）" >
          <el-input  type="text" v-model="formData2.nearest_mrt" autocomplete="off" />
        </el-form-item>

        <el-form-item label="生活圈便利店数量（单位：个）" >
          <el-input  type="text" v-model="formData2.stores" autocomplete="off" />
        </el-form-item>



        <el-form-item>
          <el-button style="margin: auto;width: 100px" type="primary" @click="submitForm2()"
          >确定</el-button
          >
          <el-button style="margin: auto;width: 100px" type="primary" @click="resetData"
          >重置数据</el-button
          >
        </el-form-item>

      </el-form>

    </template>
  </el-dialog>
</template>

<script >
import axios from "axios";
import {reactive,ref} from 'vue'
import { ElMessage ,ElMessageBox} from 'element-plus'

export default {
  data(){
    return{
      headers:{
        Authorization:localStorage.token
      },
      data:reactive([]),
      pageSize:10,
      page:1,
      sno:'',
      dialogVisible:false,
      dialogVisible2:false,
      formData:{id:' ',house_age:' ',nearest_mrt:''
        ,stores:''},
      formData2:{id:'1',house_age:'32',nearest_mrt:'84.87882'
        ,stores:'10'},
    }
  },
  methods:{

    formatDate(row, column) {
      // 获取单元格数据
      let data = row[column.property]
      if(data == null) {
        return null
      }
      let dt = new Date(data)
      return dt.getFullYear() + '-' + (dt.getMonth() + 1) + '-' + dt.getDate()
    },
    searchEnter(){
      if(!this.sno){
        this.getData()
      }
      else{
        axios.get('http://127.0.0.1:5000/home/selectSno?sno='+this.sno).then(res=>{
          if(res.data==='no data'){
            this.data=[]
            return
          }

          this.data=[...res.data]
        })
      }
    },
    handleCommand(command){
      if(command==='all'){
        this.getData()
        return
      }
      axios.get('http://127.0.0.1:5000/home/select?class='+command).then(res=>{
        this.data=[...res.data]
      })
    },
    addData(){
      this.dialogVisible2=true
      this.formData2={id:Math.round(Math.random()*1000),house_age:Math.round(Math.random()*100),nearest_mrt:Math.random()*1000
          ,stores:Math.round(Math.random()*10)}
    },
    resetData(){
      this.formData2=
          {house_age:'32',nearest_mrt:'84.87882'
            ,stores:'10',latitude:'24.98298',longitude:'121.54024'}
    },
    deleteAll(){
      axios.get("http://127.0.0.1:5000/home/delete")
          .then(res=>{
            this.getData()
            ElMessage({
              message: res.data,
              type: 'success',
            })
          })
    },
    uploadFile(param){
      let fileObj = param.file
      let form = new FormData()
      form.append("file", fileObj)
      axios.post("http://127.0.0.1:5000/home/upload",form)
          .then(res=>{
            this.getData()
            ElMessage({
              message: res.data,
              type: 'success',
            })
          })
    },
    submitForm2(){
      this.dialogVisible2=false
      axios({
        method: 'post',
        url: 'http://127.0.0.1:5000/home/add',
        data:{
          'data':this.formData2
        }
      })
          .then(res=> {
            this.getData()
            ElMessage({
              message: res.data,
              type: 'success',
            })
          })
    },
    submitForm(){
      this.dialogVisible=false

      axios({
        method: 'post',
        url: 'http://127.0.0.1:5000/home/update',
        data:{
          'data':this.formData
        }
      })
          .then(res=> {
            this.getData()
            ElMessage({
              message: '修改成功!',
              type: 'success',
            })
          })
    },
    handleEdit(row){
      this.formData=row
      this.dialogVisible=true
    },
    handleDelete(sno){
      axios.get('http://127.0.0.1:5000/home/delete/'+sno).then(res=>{
        this.data=this.data.filter(item => item.id!==sno)
        ElMessage({
          message: '删除成功!',
          type: 'success',
        })
      })
          .catch(error=>{
            alert("error");
          })
    },
    handleSizeChange(val) {
      this.pageSize=val
    },
    handleCurrentChange(val){
      this.page=val
    },
    getData(){
      axios.get('http://127.0.0.1:5000/home').then(res=>{
        if(res.data==="no data"){
          this.data=[]
          ElMessage({
            message: '请尽快导入数据!',
            type: 'success',
          })
        }else{
          this.data=[...res.data]
        }
      })
    }

  },
  mounted() {
    this.getData()
  }
}




</script>


<style scoped>

</style>