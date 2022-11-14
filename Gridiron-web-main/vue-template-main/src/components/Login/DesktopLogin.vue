<!----------------------------------------------->
<!--                  TEMPLATE                 -->
<!----------------------------------------------->
<template>
  <div
    class="main-content"
    :style="
      '--my-font-var:' +
      primaryFont +
      ';' +
      '--my-color-var:' +
      primaryColor +
      ';'
    "
  >
    <!-- Nav -->
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <a class="navbar-brand">
        <router-link to="/">
          <img class="nav-bar-logo" v-bind:src="projectLogo" alt="logo" />
        </router-link>
      </a>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto"></ul>
        <div class="form-inline my-2 my-lg-0">
          <ul class="navbar-nav mr-auto">
            <li class="nav-item">
              <router-link to="/" style="text-decoration: none">
                <a class="nav-link"><i class="fas fa-forward"></i></a>
              </router-link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
    <!-- main -->
    <div class="row main-row">
    <!-- Left -->
      <div class="col-md-5 left" :style="'--my-color-var:' + primaryColor + ';' " @click="$router.push('/')">
        <div class="main-info animation a3" :style="'--my-color-var:' + primaryColor + ';'">
          <div class="row project-name-div text-center justify-content-center">
            <div class="row justify-content-center">
              <img class="project-logo" v-bind:src="projectLogo" alt="logo"  style="margin-top:6em" />
            </div>
            <div class="row mb-0" >
              <h1 class="project-title">
                {{ projectName }}
              </h1>
            </div> 
          </div>
        </div>
      </div>
      <!-- right -->
      <div class="col-md-7 right animation animation ">
        <LoginForm />
      </div>
    </div>
  </div>
</template>

<!----------------------------------------------->
<!--                    SCRIPT                 -->
<!----------------------------------------------->

<script>
import LoginForm from "../../components/Partials/LoginForms/DesktopLoginForm";

export default {
  /* Name */
  name: "Home",
  inject: ["mq"],
  /* Data */
  data() {
    return {};
  },
  /* Components */
  components: {
    LoginForm,
  },
  /* Props */
  props: {},
  /* Methods */
  methods: {},
  mounted() {
    $("#target").click(function () {
      var left = $("#coolDiv").offset().left;
      $("#coolDiv")
        .css({
          left: left,
        })
        .animate(
          {
            left: "0px",
          },
          "slow"
        );
    });
  },
};
</script>

<script setup>
import { useMq } from "vue3-mq";
const mq = useMq();
</script>
<!----------------------------------------------->
<!--                    STYLES                 -->
<!----------------------------------------------->
<style scoped >
*{
  overflow-y: hidden;
}
.navbar {
  z-index: 999;
}
.nav-bar-logo {
  height: 2em;
}
.main-content {
  height: 100vh;
  width: 100vw;
  margin: 0;
  font-family: var(--my-font-var);
}
.main-row {
  height: 100vh;
  width: 100vw;
  background-image: url("../../assets/background-img.jpg");
  background-size: cover;
  z-index: 10;
}
.main-row:after {
  position: absolute;
  content: "";
  height: 97%;
  width: 100%;
  top: 0;
  left: 0;
  background: linear-gradient(
    to bottom,
    rgba(255, 0, 0, 0) 0%,
    var(--my-color-var) 100%
  );
  z-index: 1;
}
/*
.left {
  height: 100vh;
  background-image: url("../../assets/background-img.jpg");
  background-size: cover;
  z-index: 2;
}
*/
/*
.left:after {
    position: absolute;
    content:"";
    height:97%;
    width:100%;
    top:0;
    left:0;
    background: linear-gradient(to bottom, rgba(255,0,0,0) 0%,var(--my-color-var) 100%); 
}
*/
.right {
  background-color: #ffffff;
  z-index: 2;
}
.left{
  z-index: 2;
}
.animation {
  animation-name: move;
  animation-duration: 0.4s;
  animation-fill-mode: both;
  animation-delay: 0s;
}
.a0 {
  animation-delay: 0s;
}
.a1 {
  animation-delay: 0.5s;
}

.a2 {
  animation-delay: 0.6s;
}

.a3 {
  animation-delay: 0.7s;
}

.a4 {
  animation-delay: 0.8s;
}

.a5 {
  animation-delay: 0.9s;
}

.a6 {
  animation-delay: 1s;
}

.a7 {
  animation-delay: 1.1s;
}

@keyframes move {
  0% {
    opacity: 0;
    visibility: hidden;
    transform: translateX(100px);
  }

  100% {
    opacity: 1;
    visibility: visible;
    transform: translateY(0);
  }
}

@keyframes left {
  0% {
    opacity: 0;
    width: 0;
  }

  100% {
    opacity: 1;
    padding: 20px 40px;
    width: 440px;
  }
}

/* --------------- */
.main-info{
  padding-top: 10em;
}
.project-name-div {
  width: 100%;
}
.project-logo {
  width: 15em;
  filter: brightness(0) invert(1);
}
.project-title {
  font-weight: 100;
  color: white;
  font-size: 4em;
}
.project-subtitle {
  color: white;
  font-size: 2em;
}
.t1 {
  font-weight: 100;
  
}
.t2 {
  font-weight: 900;
}
.partners-row {
  width: 100%;
  position: absolute;
  bottom: 0;
}
.brand-logo {
  filter: brightness(0) invert(1);
  width: 7em;
  margin-bottom: 6em;
}
</style>
