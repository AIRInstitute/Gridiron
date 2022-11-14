<!----------------------------------------------->
<!--                  TEMPLATE                 -->
<!----------------------------------------------->
<template>
  <Navbar></Navbar>
  <div class="maincontainer">
    <div class="row">
      <div class="col-6">
        <Formulary :JSONform="JSONform"></Formulary>
      </div>
      <div class="col-6">
        <Table :JSONtable="JSONtable"></Table>
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
  margin-bottom: 5%;
  font-family: var(--my-font-var);
}
</style>


