webpackJsonp([6],{NHnr:function(t,e,n){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var a=n("7+uW"),o=n("9rMa");a.default.use(o.a);var r=new o.a.Store({state:{token:""},mutations:{set_token:function(t,e){t.token=e,localStorage.token=e},del_token:function(t){t.token="",localStorage.removeItem("token")}}}),u={render:function(){var t=this.$createElement,e=this._self._c||t;return e("div",{attrs:{id:"app"}},[e("router-view",[e("div",{staticClass:"header"},[this._v("\n  I am header!\n")])])],1)},staticRenderFns:[]},c=n("VU/8")(null,u,!1,function(t){n("niKH")},null,null).exports,i=n("/ocq");a.default.use(i.a);var l=new i.a({routes:[{path:"/",redirect:"/readme"},{path:"/readme",component:function(t){return n.e(0).then(function(){var e=[n("MpTN")];t.apply(null,e)}.bind(this)).catch(n.oe)},children:[{path:"/",component:function(t){return n.e(1).then(function(){var e=[n("Kblq")];t.apply(null,e)}.bind(this)).catch(n.oe)}},{path:"/count",component:function(t){return n.e(4).then(function(){var e=[n("C2yV")];t.apply(null,e)}.bind(this)).catch(n.oe)}},{path:"/users",component:function(t){return n.e(3).then(function(){var e=[n("zR98")];t.apply(null,e)}.bind(this)).catch(n.oe)}}]},{path:"/login",component:function(t){return n.e(2).then(function(){var e=[n("GF4k")];t.apply(null,e)}.bind(this)).catch(n.oe)}}]}),s=n("mtWM"),p=n.n(s),d=n("zL8q"),f=n.n(d);n("tvR6");a.default.config.debug=!0,a.default.use(f.a),a.default.prototype.$axios=p.a,p.a.defaults.auth={username:"",password:""},l.beforeEach(function(t,e,n){t.meta.required?localStorage.token?(r.commit("set_token",localStorage.token),p.a.defaults.auth={username:"localStorage.token",password:"unused"},n()):n({path:"/login"}):n()}),l.afterEach(function(t,e,n){}),new a.default({router:l,store:r,render:function(t){return t(c)}}).$mount("#app")},niKH:function(t,e){},tvR6:function(t,e){}},["NHnr"]);
//# sourceMappingURL=app.51e885a14b6393fec084.js.map