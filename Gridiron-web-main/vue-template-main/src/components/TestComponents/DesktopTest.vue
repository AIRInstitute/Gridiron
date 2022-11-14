<!----------------------------------------------->
<!--                  TEMPLATE                 -->
<!----------------------------------------------->
<template>
<div>
  <Navbar></Navbar>
  <div class="maincontainer">
    <div class="row">
      <div class="col-6">
        <h2>Data gradient</h2>
        <div class="card card-1"  >
          <iframe src="http://localhost:2900/d-solo/kuVnK4eMz/energy-charts?orgId=1&from=1637535077651&to=1637617928492&theme=light&panelId=34" width="100%" height="200" frameborder="0"></iframe>
        </div>
        <h2>Data gradient</h2>
        <div class="card card-1"  >
          <iframe src="http://localhost:2900/d-solo/kuVnK4eMz/energy-charts?orgId=1&from=1637538677000&to=1637617928000&theme=light&panelId=40" width="100%" height="200" frameborder="0"></iframe>
        </div>
      </div>
      <div class="col-6">
        <Table :JSON_table_data="JSON_table_data" :JSON_table_form="JSON_table_form"></Table>
      </div>
    </div>
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
.filtro {
  box-shadow: 0 3px 10px rgb(0 0 0 / 0.2);
  padding: 1em;
}
.date-picker {
  width: 100%;
}
.counter {
  padding: 8px;
  color: #ccc;
}
.incidence_alert {
  text-align: left;
}
h2 {
  color: #265d7e;
  font-size: 1.5em;
  font-weight: 900;
}
a {
  text-decoration: none;
  color: black;
}
.maincontainer {
  width: 100%;
  padding-right: 5%;
  padding-left: 5%;
  margin-bottom: 5em;
  font-family: var(--my-font-var);
}
</style>


