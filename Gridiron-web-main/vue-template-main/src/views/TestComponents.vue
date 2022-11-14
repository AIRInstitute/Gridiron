<!----------------------------------------------->
<!--                  TEMPLATE                 -->
<!----------------------------------------------->
<template>
  <MobileTest v-if="  mq.current  === 'mobile'"></MobileTest>
  <TabletTest v-if="  mq.current  === 'tablet'"></TabletTest>
  <DesktopTest v-if=" mq.current  === 'desktop'"></DesktopTest>
</template>

<!----------------------------------------------->
<!--                    SCRIPT                 -->
<!----------------------------------------------->
<script>
import MobileTest from "../components/TestComponents/MobileTest";
import TabletTest from "../components/TestComponents/TabletTest";
import DesktopTest from "../components/TestComponents/DesktopTest";

export default {
  /* Name */
  name: "Table",
  inject: ["mq"],
  /* Components */
  components: {
    MobileTest,
    TabletTest,
    DesktopTest,
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
