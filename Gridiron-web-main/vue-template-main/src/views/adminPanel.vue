<!----------------------------------------------->
<!--                  TEMPLATE                 -->
<!----------------------------------------------->
<template>
  <!-- <MobileProfile v-if="  mq.current  === 'mobile'"></MobileProfile> -->
  <!-- <TabletProfile v-if="  mq.current  === 'tablet'"></TabletProfile> -->
  <AddingUser v-if=" mq.current  === 'desktop'"></AddingUser>
</template>

<!----------------------------------------------->
<!--                    SCRIPT                 -->
<!----------------------------------------------->
<script>
// import MobileProfile from "../components/Profile/MobileProfile";
// import TabletProfile from "../components/Profile/TabletProfile";
import AddingUser from "../components/AdminUtils/AddingUser";

export default {
  /* Name */
  name: "Profile",
  inject: ["mq"],
  /* Components */
  components: {
    // MobileProfile,
    // TabletProfile,
    AddingUser,
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
