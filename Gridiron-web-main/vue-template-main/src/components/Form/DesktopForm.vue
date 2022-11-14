<!----------------------------------------------->
<!--                  TEMPLATE                 -->
<!----------------------------------------------->
<template>
  <Navbar></Navbar>
  <div class="maincontainer" :style="'--my-font-var:' + primaryFont + ';'">
    <div class="row text-center">
      <h2>¿Esta es una pregunta?</h2>
    </div>
    <div class="row">
      <div class="col-2 text-center">
        <i class="fas fa-chevron-left"></i>
      </div>
      <div class="col-8">
        <div class="form-check">
          <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault1">
          <label class="form-check-label" for="flexRadioDefault1">
            Default radio
          </label>
        </div>
        <div class="form-check">
          <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault2" checked>
          <label class="form-check-label" for="flexRadioDefault2">
            Default checked radio
          </label>
        </div>
      </div>
      <div class="col-2 text-center">
        <i class="fas fa-chevron-right"></i>
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
.col-2{
  font-size: 4em;
  vertical-align: middle;
}
.col-2:hover{
background-color: rgba(223, 223, 223, 0.247);
}
.maincontainer {
  width: 100%;
  padding-top: 2em;
  padding-right: 14%;
  padding-left: 14%;
  padding-bottom: 5%;
  font-family: var(--my-font-var);
}
</style>


