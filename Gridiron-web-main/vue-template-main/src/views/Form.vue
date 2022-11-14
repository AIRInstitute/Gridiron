<!----------------------------------------------->
<!--                  TEMPLATE                 -->
<!----------------------------------------------->
<template>
  <MobileForm v-if="  mq.current  === 'mobile'"></MobileForm>
  <TabletForm v-if="  mq.current  === 'tablet'"></TabletForm>
  <DesktopForm v-if=" mq.current  === 'desktop'"></DesktopForm>
</template>

<!----------------------------------------------->
<!--                    SCRIPT                 -->
<!----------------------------------------------->
<script>
import MobileForm from "../components/Form/MobileForm";
import TabletForm from "../components/Form/TabletForm";
import DesktopForm from "../components/Form/DesktopForm";

export default {
  /* Name */
  name: "Form",
  inject: ["mq"],
  /* Components */
  components: {
    MobileForm,
    TabletForm,
    DesktopForm,
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
