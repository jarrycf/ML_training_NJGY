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
      <el-button type="primary" @click="searchEnter" >搜索病例编号</el-button>
    </el-col>

    <el-col :span="3"><div class="grid-content ep-bg-purple" />
      <el-dropdown split-button type="primary" @command="handleCommand">
        选择类别
        <template #dropdown>
          <el-dropdown-menu>
            <el-dropdown-item command="no-recurrence-events">no-recurrence-events</el-dropdown-item>
            <el-dropdown-item command="recurrence-events">recurrence-events</el-dropdown-item>
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
    <el-table-column label="诊断编号" prop="id" />
    <el-table-column label="年龄" prop="age" />
    <el-table-column label="绝经期" prop="menopause" />
    <el-table-column label="肿瘤大小" prop="tumor_size" />
    <el-table-column label="淋巴结个数" prop="inv_nodes" />
    <el-table-column label="结节冒有无" prop="node_caps" />
    <el-table-column label="肿瘤恶性程度" prop="deg_malig" />
    <el-table-column label="所在象限" prop="breast_quad" />
    <el-table-column label="是否有放射性治疗经历" prop="irradiat" />
    <el-table-column label="类别" prop="class" />
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
      title="诊断信息编辑"
      width="40%"
  >
    <template #footer>
      <el-form
          class="demo-ruleForm"
      >
        <el-form-item style="width: 430px" label="&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;病例编号" >
          <el-input  type="text" v-model="formData.id"  autocomplete="off" />
        </el-form-item>

        <el-form-item label="&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;年龄" >
          <el-select v-model="formData.age" class="m-2" placeholder="请选择你的年龄区间" size="large">
            <el-option
                v-for="item in ages"
                :key="item.value"
                :label="item.label"
                :value="item.value"
            />
          </el-select>
        </el-form-item>


        <el-form-item label="&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;绝经期" >
          <el-select v-model="formData.menopause" class="m-2" placeholder="" size="large">
            <el-option
                v-for="item in menopause"
                :key="item.value"
                :label="item.label"
                :value="item.value"
            />
          </el-select>
        </el-form-item>
        <el-form-item label="&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;肿瘤大小" >
          <el-select v-model="formData.tumor_size" class="m-2" placeholder="" size="large">
            <el-option
                v-for="item in tumor_size"
                :key="item.value"
                :label="item.label"
                :value="item.value"
            />
          </el-select>
        </el-form-item>
        <el-form-item label="&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;淋巴结个数" >
          <el-select v-model="formData.inv_nodes" class="m-2" placeholder="" size="large">
            <el-option
                v-for="item in inv_nodes"
                :key="item.value"
                :label="item.label"
                :value="item.value"
            />
          </el-select>
        </el-form-item>
        <el-form-item label="&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;结节冒有无" >
          <el-select v-model="formData.node_caps" class="m-2" placeholder="" size="large">
            <el-option
                v-for="item in node_caps"
                :key="item.value"
                :label="item.label"
                :value="item.value"
            />
          </el-select>
        </el-form-item>
        <el-form-item label="&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;肿瘤恶性程度" >
          <el-select v-model="formData.deg_malig" class="m-2" placeholder="" size="large">
            <el-option
                v-for="item in deg_malig"
                :key="item.value"
                :label="item.label"
                :value="item.value"
            />
          </el-select>
        </el-form-item>
        <el-form-item label="&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;所在象限" >
          <el-select v-model="formData.breast_quad" class="m-2" placeholder="" size="large">
            <el-option
                v-for="item in breast_quad"
                :key="item.value"
                :label="item.label"
                :value="item.value"
            />
          </el-select>
        </el-form-item>
        <el-form-item label="&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;是否有放射性治疗经历" >
          <el-select v-model="formData.irradiat" class="m-2" placeholder="" size="large">
            <el-option
                v-for="item in irradiat"
                :key="item.value"
                :label="item.label"
                :value="item.value"
            />
          </el-select>
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
      title="诊断信息添加"
      width="40%"
  >
    <template #footer>
      <el-form
          class="demo-ruleForm"
      >
        <el-form-item style="width: 430px" label="&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;病例编号" >
          <el-input  type="text" v-model="formData2.id"  autocomplete="off" />
        </el-form-item>

        <el-form-item label="&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;年龄" >
          <el-select v-model="formData2.age" class="m-2" placeholder="请选择你的年龄区间" size="large">
            <el-option
                v-for="item in ages"
                :key="item.value"
                :label="item.label"
                :value="item.value"
            />
          </el-select>
        </el-form-item>


        <el-form-item label="&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;绝经期" >
          <el-select v-model="formData2.menopause" class="m-2" placeholder="" size="large">
            <el-option
                v-for="item in menopause"
                :key="item.value"
                :label="item.label"
                :value="item.value"
            />
          </el-select>
        </el-form-item>
        <el-form-item label="&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;肿瘤大小" >
          <el-select v-model="formData2.tumor_size" class="m-2" placeholder="" size="large">
            <el-option
                v-for="item in tumor_size"
                :key="item.value"
                :label="item.label"
                :value="item.value"
            />
          </el-select>
        </el-form-item>
        <el-form-item label="&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;淋巴结个数" >
          <el-select v-model="formData2.inv_nodes" class="m-2" placeholder="" size="large">
            <el-option
                v-for="item in inv_nodes"
                :key="item.value"
                :label="item.label"
                :value="item.value"
            />
          </el-select>
        </el-form-item>
        <el-form-item label="&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;结节冒有无" >
          <el-select v-model="formData2.node_caps" class="m-2" placeholder="" size="large">
            <el-option
                v-for="item in node_caps"
                :key="item.value"
                :label="item.label"
                :value="item.value"
            />
          </el-select>
        </el-form-item>
        <el-form-item label="&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;肿瘤恶性程度" >
          <el-select v-model="formData2.deg_malig" class="m-2" placeholder="" size="large">
            <el-option
                v-for="item in deg_malig"
                :key="item.value"
                :label="item.label"
                :value="item.value"
            />
          </el-select>
        </el-form-item>
        <el-form-item label="&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;所在象限" >
          <el-select v-model="formData2.breast_quad" class="m-2" placeholder="" size="large">
            <el-option
                v-for="item in breast_quad"
                :key="item.value"
                :label="item.label"
                :value="item.value"
            />
          </el-select>
        </el-form-item>
        <el-form-item label="&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;是否有放射性治疗经历" >
          <el-select v-model="formData2.irradiat" class="m-2" placeholder="" size="large">
            <el-option
                v-for="item in irradiat"
                :key="item.value"
                :label="item.label"
                :value="item.value"
            />
          </el-select>
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
      formData:{id:' ',age:' ',
        menopause:'',
        tumor_size:'',
        inv_nodes:'',
        node_caps:'',
        deg_malig:'',
        breast_quad:'',
        irradiat:'',
      },
      formData2:{id:`${Math.round(Math.random()*1000)}`,age:'10-19',
        menopause:'premeno',
        tumor_size:'0-4',
        inv_nodes:'0-2',
        node_caps:'yes',
        deg_malig:'1',
        breast_quad:'left_up',
        irradiat:'yes',
      },
      ages:[
        {
          value: '10-19',
          label: '10-19',
        },
        {
          value: '20-29',
          label: '20-29',
        },
        {
          value: '30-39',
          label: '30-39',
        },
        {
          value: '40-49',
          label: '40-49',
        },
        {
          value: '50-59',
          label: '50-59',
        },
        {
          value: '60-69',
          label: '60-69',
        },
        {
          value: '70-79',
          label: '70-79',
        },
        {
          value: '80-89',
          label: '80-89',
        },
        {
          value: '90-99',
          label: '90-99',
        },
      ],
      menopause:[
        {
          value: 'premeno',
          label: 'premeno',
        },
        {
          value: 'ge40',
          label: 'ge40',
        },
        {
          value: 'lt40',
          label: 'lt40',
        }
      ],
      irradiat:[
        {
          value: 'yes',
          label: 'yes',
        },
        {
          value: 'no',
          label: 'no',
        }
      ],
      tumor_size:[
        {
          value: '0-4',
          label: '0-4',
        },
        {
          value: '5-9',
          label: '5-9',
        },
        {
          value: '10-14',
          label: '10-14',
        }
        ,        {
          value: '15-19',
          label: '15-19',
        },
        {
          value: '20-24',
          label: '20-24',
        },
        {
          value: '25-29',
          label: '25-29',
        },
        {
          value: '30-34',
          label: '30-34',
        },
        {
          value: '35-39',
          label: '35-39',
        },
        {
          value: '40-44',
          label: '40-44',
        },
        {
          value: '50-54',
          label: '50-54',
        },
        {
          value: '55-59',
          label: '55-59',
        }
      ],
      inv_nodes:[
        {
          value: '0-2',
          label: '0-2',
        },
        {
          value: '3-5',
          label: '3-5',
        },
        {
          value: '6-8',
          label: '6-8',
        },
        {
          value: '9-11',
          label: '9-11',
        },
        {
          value: '12-14',
          label: '12-14',
        },
        {
          value: '15-17',
          label: '15-17',
        },        {
          value: '18-20',
          label: '18-20',
        },
        {
          value: '21-23',
          label: '21-23',
        },        {
          value: '24-26',
          label: '24-26',
        },        {
          value: '27-29',
          label: '27-29',
        },        {
          value: 'lt40',
          label: 'lt40',
        },        {
          value: '30-32',
          label: '30-32',
        },        {
          value: '33-35',
          label: '33-35',
        },

        {
          value: '36-39',
          label: '36-39',
        },

      ],
      node_caps:[
        {
          value: 'yes',
          label: 'yes',
        },
        {
          value: 'no',
          label: 'no',
        },

      ],
      deg_malig:[
        {
          value: '1',
          label: '1',
        },
        {
          value: '2',
          label: '2',
        },        {
          value: '3',
          label: '3',
        },

      ],
      breast_quad:[
        {
          value: 'left_up',
          label: 'left_up',
        },
        {
          value: 'left_low',
          label: 'left_low',
        },        {
          value: 'right_up',
          label: 'right_up',
        },      {
          value: 'right_low',
          label: 'right_low',
        },      {
          value: 'central',
          label: 'central',
        },

      ],

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
        axios.get('http://127.0.0.1:5000/medical/selectSno?sno='+this.sno).then(res=>{
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
      axios.get('http://127.0.0.1:5000/medical/select?class='+command).then(res=>{

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

    },
    resetData(){
      this.formData2=
          {house_age:'32',nearest_mrt:'84.87882'
            ,stores:'10',latitude:'24.98298',longitude:'121.54024'}
    },
    deleteAll(){
      axios.get("http://127.0.0.1:5000/medical/delete")
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
      axios.post("http://127.0.0.1:5000/medical/upload",form)
          .then(res=>{
            this.getData()
            ElMessage({
              message: res.data,
              type: 'success',
            })
          })
    },
    submitForm2(){
      this.formData2.id=`${Math.round(Math.random()*1000)}`
      this.dialogVisible2=false
      axios({
        method: 'post',
        url: 'http://127.0.0.1:5000/medical/add',
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
        url: 'http://127.0.0.1:5000/medical/update',
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
      axios.get('http://127.0.0.1:5000/medical/delete/'+sno).then(res=>{
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
      axios.get('http://127.0.0.1:5000/medical').then(res=>{
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