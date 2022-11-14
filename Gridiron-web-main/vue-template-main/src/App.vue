<!----------------------------------------------->
<!--                  TEMPLATE                 -->
<!----------------------------------------------->
<template>
  <router-view :key="$route.fullPath"></router-view>
  <Footer></Footer>
</template>

<!----------------------------------------------->
<!--                    SCRIPT                 -->
<!----------------------------------------------->
<script>
import Footer from "./components/Partials/Footer";

export default {
  /* Name */
  name: "App",
  inject: ["mq"],
  /* Components */
  components: {
    Footer,
  },
  /* Computed */
  computed: {
    showNavbar() {
      if (this.$route.path === "/" ){
        return false;
      } else {
        return true;
      }
    },
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
#app {
  height: 100vh;
  width: 100vw;
}
</style>
