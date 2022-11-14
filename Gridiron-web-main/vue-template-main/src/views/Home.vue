<!----------------------------------------------->
<!--                  TEMPLATE                 -->
<!----------------------------------------------->
<template>
  <HomeMobile v-if="  mq.current  === 'mobile'"></HomeMobile>
  <HomeTablet v-if="  mq.current  === 'tablet'"></HomeTablet>
  <HomeDesktop v-if=" mq.current  === 'desktop'"></HomeDesktop>
</template>

<!----------------------------------------------->
<!--                    SCRIPT                 -->
<!----------------------------------------------->
<script>
import HomeMobile from "../components/Home/MobileHome";
import HomeTablet from "../components/Home/TabletHome";
import HomeDesktop from "../components/Home/DesktopHome";

export default {
  /* Name */
  name: "Dashboard",
  inject: ["mq"],
  /* Components */
  components: {
    HomeMobile,
    HomeTablet,
    HomeDesktop,
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
</style>
