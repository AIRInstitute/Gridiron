<!----------------------------------------------->
<!--                  TEMPLATE                 -->
<!----------------------------------------------->
<template>
  <div class="main-content" :style="'--my-font-var:' + primaryFont + ';'">
    <!-- Nav --> 
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <a class="navbar-brand">
        <router-link to="/">
          <img
            class="nav-bar-logo"
            v-bind:src="projectLogo"
            alt="logo"
          />
        </router-link>
      </a>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto">
        </ul>
        <div class="form-inline my-2 my-lg-0">
          <ul class="navbar-nav mr-auto">
            <li class="nav-item">
              <router-link to="/login" style="text-decoration: none;">
                <a class="nav-link">Sign In</a>
              </router-link>
            </li> 
          </ul>
        </div>
      </div>
    </nav>
    <!-- Main content -->
    <div class="main-info" :style="'--my-color-var:' + primaryColor + ';'">
      <div class="row project-name-div text-center justify-content-center">
        <img
            class="project-logo"
            v-bind:src="projectLogo"
            alt="logo" style="margin-top:6em"
        />
        <h1 class="project-title">
          {{projectName}}
        </h1>
        <h3 class="project-subtitle">
          {{projectSubtitle}}
        </h3>
        <div class="row partners-row justify-content-center">
          <img
            v-for="logo in partners" :key="logo"
            :id="logo"
            class="brand-logo"
            :src="require('@/assets/partners/'+logo)"
            alt="logo"
        />
        </div>
      </div>
    </div> 
  </div>
</template>

<!----------------------------------------------->
<!--                    SCRIPT                 -->
<!----------------------------------------------->

<script>
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
  },
  /* Props */
  props: {},
  /* Methods */
  methods: {},
  mounted() {
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
.a{
  text-decoration: none;
}
.navbar{
  z-index: 999;
}
.main-content {
  font-family: var(--my-font-var);
  height: 100vh;
  width: 100vw;
  margin: 0;
}
.nav-bar-logo{
  height: 2em;
}
.main-info{
  width: 100%;
  height: 90%;
  background-image: url("../../assets/background-img.jpg");
  background-size: cover;
  padding-top: 7em;
}
.main-info:after {
    position: absolute;
    content:"";
    height:97%;
    width:100%;
    top:0;
    left:0;
    background: linear-gradient(to bottom, rgba(255,0,0,0) 0%, var(--my-color-var) 90%); /* W3C */ 
}
.sec-info{
  padding-left: 15%;
  padding-right: 15%;
  padding-bottom: 15em;
}
.project-name-div{
  width: 100%;
}
.project-logo{
  z-index: 999;
  width: 20em;
  filter:  brightness(0) invert(1);
}
.project-title{
  font-weight: 100;
  z-index: 999;
  color: white;
  font-size: 4em;
  margin-top: .5em;
}
.project-subtitle{
  color: white;
  z-index: 999;
  font-size: 2em;
}
.t1{
  font-weight: 100;
}
.t2{
  font-weight: 900;
}
.partners-row{
  width: 100%;
  position: absolute; 
  bottom: 0;
}
.brand-logo{
    filter:  brightness(0) invert(1);
    width: 7em;
    z-index: 999;
    margin-bottom: 6em;
}
</style>
