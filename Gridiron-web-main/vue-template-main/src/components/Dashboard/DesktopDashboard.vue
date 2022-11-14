<!----------------------------------------------->
<!--                  TEMPLATE                 -->
<!----------------------------------------------->
<template>
  <Navbar></Navbar>
  <div class="main-content" :style="'--my-font-var:' + primaryFont + ';'">
    <div class="maincontainer">
      <div class="cards">
        <router-link to="/test">
         <div class="card card-1" :style="'--my-color-var:' + primaryColor + ';'">
            <div class="card__icon"><i class="fas fa-chart-line"></i></div>
            <h2 class="card__title">Data Visualization</h2>
          </div>
        </router-link>
        <router-link to="/microscope">
         <div class="card card-1" :style="'--my-color-var:' + primaryColor + ';'">
            <div class="card__icon"><i class="fas fa-microscope"></i></div>
            <h2 class="card__title">Microscope Robot</h2>
          </div>
        </router-link>
        <router-link to="/protocols">
         <div class="card card-1" :style="'--my-color-var:' + primaryColor + ';'">
            <div class="card__icon"><i class="fas fa-eye-dropper"></i></div>
            <h2 class="card__title">Liquid Handling Robot</h2>
          </div>
        </router-link>
      </div>
    </div>
  </div>
</template>

<!----------------------------------------------->
<!--                    SCRIPT                 -->
<!----------------------------------------------->
<script>
import Navbar from "../../components/Partials/Navbar";

export default {
  /* Name */
  name: "MainDesktop",
  /* Data */
  data() {
    return {};
  },
  /* Components */
  components: {
    Navbar,
  },
  /* Props */
  props: {},
  /* Methods */
  methods: {
    methodName(methodParam) {
      /* Here method logic */
    },
  },
  /* Emits */
  emits: ["emits", "emits"],
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
  padding-right: 15%;
  padding-left: 15%;
}
.cards {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}

.card {
  margin: 20px;
  padding: 20px;
  width: 400px;
  min-height: 300px;
  display: grid;
  grid-template-rows: 20px 50px 1fr 50px;
  border-radius: 10px;
  box-shadow: 0px 6px 10px rgba(0, 0, 0, 0.25);
  transition: all 0.2s;
  text-align: center;
}

.card:hover {
  box-shadow: 0px 6px 10px rgba(0, 0, 0, 0.4);
  transform: scale(1.01);
}

.card__link,
.card__icon {
  position: relative;
  text-decoration: none;
  color: rgba(255, 255, 255, 0.9);
}

.card__link::after {
  position: absolute;
  top: 25px;
  left: 0;
  content: "";
  width: 0%;
  height: 3px;
  background-color: rgba(255, 255, 255, 0.6);
  transition: all 0.5s;
}

.card__link:hover::after {
  width: 100%;
}

.card__icon {
  grid-row: 1/3;
  font-size: 8em;
}

.card__title {
  grid-row: 4/4;
  font-weight: 400;
  color: #ffffff;
}

.card__apply {
  grid-row: 4/5;
  align-self: center;
}
/* CARD BACKGROUNDS */
.card-1 {
  background: radial-gradient(var(--my-color-var), var(--my-color-var));
}
/* RESPONSIVE */
@media (max-width: 1600px) {
  .cards {
    justify-content: center;
  }
}
</style>


