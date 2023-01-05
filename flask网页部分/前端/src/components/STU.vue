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
                v-model.number="sno" placeholder="Please input" @keyup.enter="searchEnter"/>
    </el-col>
    <el-col :span="2"><div class="grid-content ep-bg-purple-light" />
      <el-button type="primary" @click="searchEnter" >搜索学号</el-button>

    </el-col>
    <el-col :span="3"><div class="grid-content ep-bg-purple" />
      <el-dropdown split-button type="primary" @command="handleCommand">
        选择类别
        <template #dropdown>
          <el-dropdown-menu>
            <el-dropdown-item command="all good">all good</el-dropdown-item>
            <el-dropdown-item command="low chinese">low chinese</el-dropdown-item>
            <el-dropdown-item command="low math">low math</el-dropdown-item>
            <el-dropdown-item command="all low">all low</el-dropdown-item>
            <el-dropdown-item command="all">all</el-dropdown-item>
          </el-dropdown-menu>
        </template>
      </el-dropdown>

    </el-col>
    <el-col :span="2"><div class="grid-content ep-bg-purple-light" />
      <el-button type="primary" @click="addData" >新增数据</el-button>

    </el-col>
  </el-row>


  <el-table :data="data.slice((page-1)*pageSize,page*pageSize)" style="width: 100%">
    <el-table-column label="学号" prop="sno" />
    <el-table-column label="Chinese" prop="chinese" />
    <el-table-column label="Math" prop="math" />
    <el-table-column label="成绩分类" prop="class" />
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
            @confirm="handleDelete(scope.row.sno)"
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
      title="学生信息编辑"
      width="30%"
      :before-close="handleClose"
  >
    <template #footer>
      <el-form
          class="demo-ruleForm"
      >


        <el-form-item label="语文成绩" >
          <el-input  type="text" v-model.number="formData.chinese" autocomplete="off" />
        </el-form-item>

        <el-form-item label="数学成绩" >
          <el-input  type="text" v-model.number="formData.math" autocomplete="off" />
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
      title="学生信息添加"
      width="30%"
      :before-close="handleClose"
  >
    <template #footer>
      <el-form
          class="demo-ruleForm"
      >
        <el-form-item label="&nbsp;&nbsp;&nbsp;&nbsp;学号&nbsp;&nbsp;&nbsp;" >
          <el-input  type="text" v-model.number="formData2.sno" autocomplete="off" />
        </el-form-item>

        <el-form-item label="语文成绩" >
          <el-input  type="text" v-model.number="formData2.chinese" autocomplete="off" />
        </el-form-item>

        <el-form-item label="数学成绩" >
          <el-input  type="text" v-model.number="formData2.math" autocomplete="off" />
        </el-form-item>

        <el-form-item>
          <el-button style="margin: auto;width: 100px" type="primary" @click="submitForm2()"
          >确认添加</el-button
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
      dialogVisible:false,
      dialogVisible2:false,
      formData:{sno:'11',chinese:'22',math:'33'},
      formData2:{sno:'',chinese:'',math:''},
      sno:''
    }
  },
  methods:{
    searchEnter(){
      if(!this.sno){
        this.getData()
      }
      else{
        axios.get('http://127.0.0.1:5000/stu/selectSno?sno='+this.sno).then(res=>{
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
      axios.get('http://127.0.0.1:5000/stu/select?class='+command).then(res=>{
        if(res.data==='no data'){
          ElMessage({
            message: "暂无数据!",
            type: 'success',
          })
          this.data=[]
          return
        }
        this.data=[...res.data]
      })
    },
    addData(){
      this.dialogVisible2=true
      this.formData2={sno:Math.round(Math.random()*1000),chinese:Math.round(Math.random()*100),math:Math.round(Math.random()*100)}
    },
    deleteAll(){
      axios.get("http://127.0.0.1:5000/stu/delete")
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
      axios.post("http://127.0.0.1:5000/stu/upload",form)
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
        url: 'http://127.0.0.1:5000/stu/add',
        data:{
          'data':this.formData2
        }
      })
          .then(res=> {
            this.getData()
            ElMessage({
              message: '添加成功!',
              type: 'success',
            })
          })
    },
    submitForm(){
      this.dialogVisible=false

      axios({
        method: 'post',
        url: 'http://127.0.0.1:5000/stu/update',
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
      axios.get('http://127.0.0.1:5000/stu/delete/'+sno).then(res=>{
        this.data=this.data.filter(item => item.sno!==sno)
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
      axios.get('http://127.0.0.1:5000/stu').then(res=>{
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