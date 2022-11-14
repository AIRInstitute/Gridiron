<!----------------------------------------------->
<!--                  TEMPLATE                 -->
<!----------------------------------------------->
<template>
  <NavbarMobile> </NavbarMobile>
  <div class="main-content" :style="'--my-font-var:' + primaryFont + ';'">
    <div class="maincontainer">
        <Table :JSON_table_data="JSON_table_data" :JSON_table_form="JSON_table_form" :add_option="true" :crud_option="true"></Table>
    </div>
  </div>
</template>

<!----------------------------------------------->
<!--                    SCRIPT                 -->
<!----------------------------------------------->
<script>
import MyShared from "./shared";

export default {
  mixins: [MyShared],
};
</script>


<!----------------------------------------------->
<!--                    STYLES                 -->
<!----------------------------------------------->
<style scoped>
.main-content {
  font-family: var(--my-font-var);
  height: 100vh;
  width: 100vw;
  margin: 0;
}
a {
  text-decoration: none;
}
.maincontainer {
  width: 100%;
  padding-top: 2.5%;
  padding-right: 2%;
  padding-left: 2%;
}
</style>


