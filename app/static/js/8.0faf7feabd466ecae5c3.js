webpackJsonp([8],{eQ1J:function(e,t,a){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var o=a("vLgD");var i={data:function(){return{url:"/api/v2.0/dict",tableData:[],dialogFormVisible:!1,dialogForm1Visible:!1,currentPage:1,pageSize:10,keys:"",form:{father:"",key:"",value:""},form1:{father:"",key:"",value:"",id:""},formLabelWidth:"120px",pageTotal:0}},created:function(){this.getData(this.currentPage,this.pageSize,this.keys)},methods:{keysEdit:function(){this.keys=this.input5,this.getData(this.currentPage,this.pageSize,this.keys)},onSubmit:function(){var e,t=this;console.log(this.form),(e=this.form,Object(o.a)({url:"/api/v2.0/dict",method:"post",data:e})).then(function(e){t.dialogFormVisible=!1,t.$message.success("提交成功！"),t.getData(t.currentPage,t.pageSize),t.form.father="",t.form.key="",t.form.value=""},function(e){t.$message.success("提交失败！")})},form1onSubmit:function(){var e,t=this;(e=this.form1,Object(o.a)({url:"/api/v2.0/dict/"+e.id,method:"put",data:e})).then(function(e){t.dialogForm1Visible=!1,t.$message.success("提交成功！"),t.getData(t.currentPage,t.pageSize)},function(e){t.$message.success("提交失败！")})},getData:function(e,t,a){var i,l=this;console.log(e),(i={page:e,size:t,keys:a},Object(o.a)({url:"/api/v2.0/dict",method:"get",params:i})).then(function(e){l.tableData=e.data.list,l.pageTotal=e.data.total,l.currentPage=e.data.page,l.pageSize=e.data.size},function(e){})},indexMethod:function(e){return e+1},handleEdit:function(e,t){this.form1.father=t.father,this.form1.key=t.key,this.form1.value=t.value,this.form1.id=t.id,this.dialogForm1Visible=!0},handleDelete:function(e,t,a){var i,l=this;(i="/api/v2.0/dict/del/"+t.id,Object(o.a)({url:i,method:"get"})).then(function(o){l.$message.success(t.key+" 删除成功！"),a.splice(e,1)},function(e){l.$message.success(t.key+" 删除失败！")})},handleSizeChange:function(e){console.log("每页 "+e+" 条"+this.currentPage+"页"),this.$options.methods.getData.bind(this)(this.currentPage,e,this.keys)},handleCurrentChange:function(e){console.log(this.pageSize),console.log(e),this.$options.methods.getData.bind(this)(e,this.pageSize,this.keys)},handleClose:function(e){this.$confirm("确认关闭？").then(function(t){e()}).catch(function(e){})}}},l={render:function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",[a("div",[a("el-row",[a("el-col",{attrs:{span:22}},[a("el-input",{attrs:{placeholder:"请输入内容"},model:{value:e.input5,callback:function(t){e.input5=t},expression:"input5"}},[a("el-button",{attrs:{slot:"append",icon:"el-icon-search"},on:{click:e.keysEdit},slot:"append"})],1)],1),e._v(" "),a("el-col",{attrs:{span:2}},[a("el-button",{on:{click:function(t){e.dialogFormVisible=!0}}},[a("i",{staticClass:"el-icon-edit"}),e._v("添加")])],1)],1)],1),e._v(" "),a("div",[a("el-dialog",{attrs:{title:"新增",visible:e.dialogFormVisible},on:{"update:visible":function(t){e.dialogFormVisible=t}}},[a("el-form",{attrs:{model:e.form}},[a("el-form-item",{attrs:{label:"父节点","label-width":e.formLabelWidth}},[a("el-input",{attrs:{"auto-complete":"off"},model:{value:e.form.father,callback:function(t){e.$set(e.form,"father",t)},expression:"form.father"}})],1),e._v(" "),a("el-form-item",{attrs:{label:"键","label-width":e.formLabelWidth}},[a("el-input",{attrs:{"auto-complete":"off"},model:{value:e.form.key,callback:function(t){e.$set(e.form,"key",t)},expression:"form.key"}})],1),e._v(" "),a("el-form-item",{attrs:{label:"值","label-width":e.formLabelWidth}},[a("el-input",{attrs:{"auto-complete":"off"},model:{value:e.form.value,callback:function(t){e.$set(e.form,"value",t)},expression:"form.value"}})],1)],1),e._v(" "),a("div",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[a("el-button",{on:{click:function(t){e.dialogFormVisible=!1}}},[e._v("取 消")]),e._v(" "),a("el-button",{attrs:{type:"primary"},on:{click:e.onSubmit}},[e._v("确 定")])],1)],1)],1),e._v(" "),a("div",[a("el-dialog",{attrs:{title:"编辑",visible:e.dialogForm1Visible},on:{"update:visible":function(t){e.dialogForm1Visible=t}}},[a("el-form",{attrs:{model:e.form}},[a("el-form-item",{attrs:{label:"父节点","label-width":e.formLabelWidth}},[a("el-input",{attrs:{"auto-complete":"off"},model:{value:e.form1.father,callback:function(t){e.$set(e.form1,"father",t)},expression:"form1.father"}})],1),e._v(" "),a("el-form-item",{attrs:{label:"键","label-width":e.formLabelWidth}},[a("el-input",{attrs:{"auto-complete":"off"},model:{value:e.form1.key,callback:function(t){e.$set(e.form1,"key",t)},expression:"form1.key"}})],1),e._v(" "),a("el-form-item",{attrs:{label:"值","label-width":e.formLabelWidth}},[a("el-input",{attrs:{"auto-complete":"off"},model:{value:e.form1.value,callback:function(t){e.$set(e.form1,"value",t)},expression:"form1.value"}})],1)],1),e._v(" "),a("div",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[a("el-button",{on:{click:function(t){e.dialogFormVisible=!1}}},[e._v("取 消")]),e._v(" "),a("el-button",{attrs:{type:"primary"},on:{click:e.form1onSubmit}},[e._v("确 定")])],1)],1)],1),e._v(" "),a("el-table",{staticStyle:{width:"100%"},attrs:{data:e.tableData}},[a("el-table-column",{attrs:{type:"index",index:e.indexMethod}}),e._v(" "),a("el-table-column",{attrs:{prop:"father",label:"父节点",sortable:""}}),e._v(" "),a("el-table-column",{attrs:{prop:"key",label:"键",sortable:""}}),e._v(" "),a("el-table-column",{attrs:{prop:"value",label:"值"}}),e._v(" "),a("el-table-column",{attrs:{prop:"head_img",label:"操作"},scopedSlots:e._u([{key:"default",fn:function(t){return[a("el-button",{attrs:{size:"mini"},on:{click:function(a){e.handleEdit(t.$index,t.row)}}},[e._v("编辑")]),e._v(" "),a("el-button",{attrs:{size:"mini",type:"danger"},on:{click:function(a){e.handleDelete(t.$index,t.row,e.tableData)}}},[e._v("删除")])]}}])})],1),e._v(" "),a("div",{staticClass:"block"},[a("el-pagination",{attrs:{"current-page":e.currentPage,"page-sizes":[10,20,50,100],"page-size":10,layout:"total, sizes, prev, pager, next, jumper",total:e.pageTotal},on:{"size-change":e.handleSizeChange,"current-change":e.handleCurrentChange}})],1)],1)},staticRenderFns:[]},s=a("VU/8")(i,l,!1,null,null,null);t.default=s.exports}});