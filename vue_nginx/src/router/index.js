import Vue from "vue";
import VueRouter from "vue-router";
import HelloWorld from "../views/HelloWorld.vue";

Vue.use(VueRouter);
const routes = [
  {
    // default path
    path: "",
    name: "HelloWorld",
    component: HelloWorld,
  },
  {
    path: "/user",
    name: "Profile",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/Profile.vue"),
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
  linkExactActiveClass: "is-active",
});

export default router;
