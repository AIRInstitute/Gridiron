<!----------------------------------------------->
<!--                  TEMPLATE                 -->
<!----------------------------------------------->
<template>
  <MobileLogin v-if="  mq.current  === 'mobile'"></MobileLogin>
  <TabletLogin v-if="  mq.current  === 'tablet'"></TabletLogin>
  <DesktopLogin v-if=" mq.current  === 'desktop'"></DesktopLogin>
</template>

<!----------------------------------------------->
<!--                    SCRIPT                 -->
<!----------------------------------------------->
<script>
import MobileLogin from "../components/Login/MobileLogin";
import DesktopLogin from "../components/Login/DesktopLogin";
import TabletLogin from "../components/Login/TabletLogin";

export default {
  /* Name */
  name: "Home",
  inject: ["mq"],
  /* Components */
  components: {
    MobileLogin,
    TabletLogin,
    DesktopLogin,
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
