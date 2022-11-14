<!----------------------------------------------->
<!--                  TEMPLATE                 -->
<!----------------------------------------------->
<template>
<div class="">
  <DesktopProtocols v-if=" mq.current  === 'desktop'"></DesktopProtocols>
</div>
</template>

<!----------------------------------------------->
<!--                    SCRIPT                 -->
<!----------------------------------------------->
<script>

import DesktopProtocols from "../components/Microscope/DesktopMicroscope";

export default {
  /* Name */
  name: "Microscope",
  inject: ["mq"],
  /* Components */
  components: {
    DesktopProtocols,
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