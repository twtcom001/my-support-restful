webpackJsonp([0],{"0tRi":function(e,t){},MpTN:function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var o={data:function(){return{name:""}},computed:{username:function(){var e=localStorage.getItem("ms_username");return e||this.name}},methods:{handleCommand:function(e){"loginout"==e&&(console.log("logout"),localStorage.removeItem("ms_username"),localStorage.removeItem("token"),this.$router.push("/login"))}}},s={render:function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{staticClass:"header"},[n("div",{staticClass:"logo"},[e._v("后台管理系统")]),e._v(" "),n("div",{staticClass:"user-info"},[n("el-dropdown",{attrs:{trigger:"click"},on:{command:e.handleCommand}},[n("span",{staticClass:"el-dropdown-link"},[e._v("\n                "+e._s(e.username)+"\n            ")]),e._v(" "),n("el-dropdown-menu",{attrs:{slot:"dropdown"},slot:"dropdown"},[n("el-dropdown-item",{attrs:{command:"loginout"}},[e._v("退出")])],1)],1)],1)])},staticRenderFns:[]},i={data:function(){return{items:[{icon:"el-icon-setting",index:"readme",title:"自述"},{icon:"el-icon-loading",index:"9",title:"成本管理",subs:[{index:"pcount",title:"清蒸庄园"},{index:"qcount",title:"吃饱饱"}]},{icon:"el-icon-menu",index:"10",title:"后台管理",subs:[{index:"users",title:"用户管理"}]}]}},computed:{onRoutes:function(){return this.$route.path.replace("/","")}},methods:{handleOpen:function(e,t){console.log(e,t)},handleClose:function(e,t){console.log(e,t)}}},a={render:function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{staticClass:"sidebar"},[n("el-menu",{staticClass:"el-menu-vertical-demo",attrs:{"default-active":e.onRoutes,theme:"dark","unique-opened":"",router:""}},[e._l(e.items,function(t){return[t.subs?[n("el-submenu",{attrs:{index:t.index}},[n("template",{slot:"title"},[n("i",{class:t.icon}),e._v(e._s(t.title))]),e._v(" "),e._l(t.subs,function(t,o){return n("el-menu-item",{key:o,attrs:{index:t.index}},[e._v(e._s(t.title)+"\n                    ")])})],2)]:[n("el-menu-item",{attrs:{index:t.index}},[n("i",{class:t.icon}),e._v(e._s(t.title)+"\n                ")])]]})],2)],1)},staticRenderFns:[]},r={components:{vHead:n("VU/8")(o,s,!1,function(e){n("R9x9")},"data-v-76ad19cb",null).exports,vSidebar:n("VU/8")(i,a,!1,function(e){n("0tRi")},"data-v-3b5540f7",null).exports},data:function(){return{url:"/api/v1.0/authtoken"}},created:function(){this.$axios.defaults.auth.username=localStorage.token,this.auth()},methods:{auth:function(){var e=this;this.$axios.get(this.url,{params:{token:localStorage.token}}).then(function(t){t.data.status||(localStorage.removeItem("ms_username"),localStorage.removeItem("token"),e.$router.push("/login"))},function(t){e.$router.push("/login")})}}},l={render:function(){var e=this.$createElement,t=this._self._c||e;return t("div",{staticClass:"wrapper"},[t("v-head"),this._v(" "),t("v-sidebar"),this._v(" "),t("div",{staticClass:"content"},[t("transition",{attrs:{name:"move",mode:"out-in"}},[t("router-view")],1)],1)],1)},staticRenderFns:[]},u=n("VU/8")(r,l,!1,null,null,null);t.default=u.exports},R9x9:function(e,t){}});
//# sourceMappingURL=0.2a657010023f77ef34cc.js.map