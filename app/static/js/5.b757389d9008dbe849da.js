webpackJsonp([5],{Cbxn:function(e,t,a){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var o=a("vLgD");var l={data:function(){return{url:"/api/v2.0/users",tableData:[],dialogFormVisible:!1,dialogForm1Visible:!1,currentPage:1,pageSize:10,form:{username:"",nickname:"",password:"",role:"2"},form1:{username:"",nickname:"",password:"",role:"",id:""},formLabelWidth:"120px",pageTotal:0}},created:function(){this.getData(this.currentPage,this.pageSize)},methods:{onSubmit:function(){var e,t=this;console.log(this.form),(e=this.form,Object(o.a)({url:"/api/v2.0/users",method:"post",data:e})).then(function(e){t.dialogFormVisible=!1,t.$message.success("提交成功！"),t.getData(t.currentPage,t.pageSize),t.form.username="",t.form.nickname="",t.form.password="",t.form.role="2"},function(e){t.$message.success("提交失败！")})},form1onSubmit:function(){var e,t=this;(e=this.form1,Object(o.a)({url:"/api/v2.0/users/"+e.id,method:"put",data:e})).then(function(e){t.dialogForm1Visible=!1,t.$message.success("提交成功！"),t.getData(t.currentPage,t.pageSize)},function(e){t.$message.success("提交失败！")})},getData:function(e,t){var a,l=this;console.log(e),(a={page:e,size:t},Object(o.a)({url:"/api/v2.0/users",method:"get",params:a})).then(function(e){l.tableData=e.data.list,l.pageTotal=e.data.total,l.currentPage=e.data.page,l.pageSize=e.data.size},function(e){})},indexMethod:function(e){return e+1},handleEdit:function(e,t){this.form1.username=t.username,this.form1.nickname=t.nickname,this.form1.role=t.role,this.form1.id=t.id,this.dialogForm1Visible=!0},handleDelete:function(e,t,a){var l,i=this;(l="/api/v2.0/users/del/"+t.id,Object(o.a)({url:l,method:"get"})).then(function(o){i.$message.success(t.username+" 删除成功！"),a.splice(e,1)},function(e){i.$message.success(t.username+" 删除失败！")})},handleSizeChange:function(e){console.log("每页 "+e+" 条"+this.currentPage+"页"),this.$options.methods.getData.bind(this)(this.currentPage,e)},handleCurrentChange:function(e){console.log(this.pageSize),console.log(e),this.$options.methods.getData.bind(this)(e,this.pageSize)},handleClose:function(e){this.$confirm("确认关闭？").then(function(t){e()}).catch(function(e){})}}},i={render:function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",[a("div",[a("span",{staticStyle:{float:"left"}},[a("el-button",{attrs:{type:"text"},on:{click:function(t){e.dialogFormVisible=!0}}},[e._v("新增用户")])],1),e._v(" "),a("el-dialog",{attrs:{title:"新增用户",visible:e.dialogFormVisible},on:{"update:visible":function(t){e.dialogFormVisible=t}}},[a("el-form",{attrs:{model:e.form}},[a("el-form-item",{attrs:{label:"用户名","label-width":e.formLabelWidth}},[a("el-input",{attrs:{"auto-complete":"off"},model:{value:e.form.username,callback:function(t){e.$set(e.form,"username",t)},expression:"form.username"}})],1),e._v(" "),a("el-form-item",{attrs:{label:"昵称","label-width":e.formLabelWidth}},[a("el-input",{attrs:{"auto-complete":"off"},model:{value:e.form.nickname,callback:function(t){e.$set(e.form,"nickname",t)},expression:"form.nickname"}})],1),e._v(" "),a("el-form-item",{attrs:{label:"密码","label-width":e.formLabelWidth}},[a("el-input",{attrs:{"auto-complete":"off"},model:{value:e.form.password,callback:function(t){e.$set(e.form,"password",t)},expression:"form.password"}})],1),e._v(" "),a("el-form-item",{attrs:{label:"角色","label-width":e.formLabelWidth}},[a("el-select",{attrs:{placeholder:"普通用户"},model:{value:e.form.role,callback:function(t){e.$set(e.form,"role",t)},expression:"form.role"}},[a("el-option",{attrs:{label:"普通用户",value:"2"}}),e._v(" "),a("el-option",{attrs:{label:"管理员",value:"1"}})],1)],1)],1),e._v(" "),a("div",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[a("el-button",{on:{click:function(t){e.dialogFormVisible=!1}}},[e._v("取 消")]),e._v(" "),a("el-button",{attrs:{type:"primary"},on:{click:e.onSubmit}},[e._v("确 定")])],1)],1)],1),e._v(" "),a("div",[a("el-dialog",{attrs:{title:"编辑用户",visible:e.dialogForm1Visible},on:{"update:visible":function(t){e.dialogForm1Visible=t}}},[a("el-form",{attrs:{model:e.form}},[a("el-form-item",{attrs:{label:"昵称","label-width":e.formLabelWidth}},[a("el-input",{attrs:{"auto-complete":"off"},model:{value:e.form1.nickname,callback:function(t){e.$set(e.form1,"nickname",t)},expression:"form1.nickname"}})],1),e._v(" "),a("el-form-item",{attrs:{label:"密码","label-width":e.formLabelWidth}},[a("el-input",{attrs:{"auto-complete":"off"},model:{value:e.form1.password,callback:function(t){e.$set(e.form1,"password",t)},expression:"form1.password"}})],1),e._v(" "),a("el-form-item",{attrs:{label:"角色","label-width":e.formLabelWidth}},[a("el-select",{attrs:{placeholder:"普通用户"},model:{value:e.form1.role,callback:function(t){e.$set(e.form1,"role",t)},expression:"form1.role"}},[a("el-option",{attrs:{label:"普通用户",value:"2"}}),e._v(" "),a("el-option",{attrs:{label:"管理员",value:"1"}})],1)],1)],1),e._v(" "),a("div",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[a("el-button",{on:{click:function(t){e.dialogFormVisible=!1}}},[e._v("取 消")]),e._v(" "),a("el-button",{attrs:{type:"primary"},on:{click:e.form1onSubmit}},[e._v("确 定")])],1)],1)],1),e._v(" "),a("el-table",{staticStyle:{width:"100%"},attrs:{data:e.tableData}},[a("el-table-column",{attrs:{type:"index",index:e.indexMethod}}),e._v(" "),a("el-table-column",{attrs:{prop:"username",label:"用户名",sortable:""}}),e._v(" "),a("el-table-column",{attrs:{prop:"nickname",label:"昵称",sortable:""}}),e._v(" "),a("el-table-column",{attrs:{prop:"head_img",label:"头像"}}),e._v(" "),a("el-table-column",{attrs:{prop:"role_id",label:"角色"}}),e._v(" "),a("el-table-column",{attrs:{prop:"last_login",label:"最后登录",sortable:""}}),e._v(" "),a("el-table-column",{attrs:{prop:"head_img",label:"操作"},scopedSlots:e._u([{key:"default",fn:function(t){return[a("el-button",{attrs:{size:"mini"},on:{click:function(a){e.handleEdit(t.$index,t.row)}}},[e._v("编辑")]),e._v(" "),a("el-button",{attrs:{size:"mini",type:"danger"},on:{click:function(a){e.handleDelete(t.$index,t.row,e.tableData)}}},[e._v("删除")])]}}])})],1),e._v(" "),a("div",{staticClass:"block"},[a("el-pagination",{attrs:{"current-page":e.currentPage,"page-sizes":[10,20,50,100],"page-size":10,layout:"total, sizes, prev, pager, next, jumper",total:e.pageTotal},on:{"size-change":e.handleSizeChange,"current-change":e.handleCurrentChange}})],1)],1)},staticRenderFns:[]},r=a("VU/8")(l,i,!1,null,null,null);t.default=r.exports}});