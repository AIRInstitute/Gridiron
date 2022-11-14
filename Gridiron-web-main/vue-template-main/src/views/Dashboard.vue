<!----------------------------------------------->
<!--                  TEMPLATE                 -->
<!----------------------------------------------->
<template>
  <!-- <MobileDashboard v-if="  mq.current  === 'mobile'"></MobileDashboard> -->
  <!-- <TabletDashboard v-if="  mq.current  === 'tablet'"></TabletDashboard> -->
  <DesktopDashboard v-if=" mq.current  === 'desktop'"></DesktopDashboard>
</template>

<!----------------------------------------------->
<!--                    SCRIPT                 -->
<!----------------------------------------------->
<script>
// import MobileDashboard from "../components/Dashboard/MobileDashboard";
// import TabletDashboard from "../components/Dashboard/TabletDashboard";
import DesktopDashboard from "../components/Dashboard/DesktopDashboard";

export default {
  /* Name */
  name: "Dashboard",
  inject: ["mq"],
  /* Components */
  components: {
    // MobileDashboard,
    // TabletDashboard,
    DesktopDashboard,
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
