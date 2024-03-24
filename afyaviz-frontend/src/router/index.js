import { createRouter, createWebHistory } from "vue-router";
import Dashboard from "../views/Dashboard.vue";
import Login from "../views/Login.vue";
import Register from "../views/Register.vue";
import Reports from "../views/Reports.vue";

const routes = [
  {
    meta: {
      title: "Dashboard",
    },
    path: "/",
    name: "dashboard",
    component: Dashboard,
  },
  {
    meta: {
      title: "Reports",
    },
    path: "/reports",
    name: "reports",
    component: Reports,
  },
  {
    meta: {
      title: "Login",
    },
    path: "/login",
    name: "/login",
    component: Login,
  },
  {
    meta: {
      title: "Register",
    },
    path: "/register",
    name: "/register",
    component: Register,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

// app.use(router);
export default router;
