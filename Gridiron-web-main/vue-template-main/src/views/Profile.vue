<!----------------------------------------------->
<!--                  TEMPLATE                 -->
<!----------------------------------------------->
<template>
  <MobileProfile v-if="  mq.current  === 'mobile'"></MobileProfile>
  <TabletProfile v-if="  mq.current  === 'tablet'"></TabletProfile>
  <DesktopProfile v-if=" mq.current  === 'desktop'"></DesktopProfile>
</template>

<!----------------------------------------------->
<!--                    SCRIPT                 -->
<!----------------------------------------------->
<script>
import MobileProfile from "../components/Profile/MobileProfile";
import TabletProfile from "../components/Profile/TabletProfile";
import DesktopProfile from "../components/Profile/DesktopProfile";

export default {
  /* Name */
  name: "Profile",
  inject: ["mq"],
  /* Components */
  components: {
    MobileProfile,
    TabletProfile,
    DesktopProfile,
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
