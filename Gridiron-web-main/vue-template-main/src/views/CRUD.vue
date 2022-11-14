<!----------------------------------------------->
<!--                  TEMPLATE                 -->
<!----------------------------------------------->
<template>
  <MobileCRUD v-if="  mq.current  === 'mobile'"></MobileCRUD>
  <TabletCRUD v-if="  mq.current  === 'tablet'"></TabletCRUD>
  <DesktopCRUD v-if=" mq.current  === 'desktop'"></DesktopCRUD>
</template>

<!----------------------------------------------->
<!--                    SCRIPT                 -->
<!----------------------------------------------->
<script>
import MobileCRUD from "../components/CRUD/MobileCRUD";
import TabletCRUD from "../components/CRUD/TabletCRUD";
import DesktopCRUD from "../components/CRUD/DesktopCRUD";

export default {
  /* Name */
  name: "CRUD",
  inject: ["mq"],
  /* Components */
  components: {
    MobileCRUD,
    TabletCRUD,
    DesktopCRUD,
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
