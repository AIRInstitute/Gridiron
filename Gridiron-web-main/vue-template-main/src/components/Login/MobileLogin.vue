<!----------------------------------------------->
<!--                  TEMPLATE                 -->
<!----------------------------------------------->
<template>
  <div class="main-content" :style="'--my-font-var:' + primaryFont + ';'">
    <div class="row main-row" :style="'--my-color-var:' + primaryColor + ';'">
      <div class="row justify-content-center">
        <img class="project-logo" v-bind:src="projectLogo" alt="logo" />
      </div>
      <LoginForm style="z-index: 999; margin-top:-3em;" />
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
  created() {},
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
.project-logo {
  width: 13em;
  filter: brightness(0) invert(1);
  z-index: 999;
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
  height: 110%;
  width: 100%;
  top: 0;
  left: 0;
  background: linear-gradient(
    to bottom,
    rgba(255, 0, 0, 0) 0%,
    var(--my-color-var) 100%
  );
}
.row {
  --bs-gutter-x: 0;
}
.main-content {
  height: 100vh;
  width: 100vw;
  font-family: var(--my-font-var);
}
.main-row {
  height: 100vh;
  width: 100vw;
}
</style>
