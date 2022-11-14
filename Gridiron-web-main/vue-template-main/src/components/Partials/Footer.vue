<!----------------------------------------------->
<!--                  TEMPLATE                 -->
<!----------------------------------------------->
<template>
  <div class="row footer">
    <p>{{footerCopyRight}}</p>
  </div>
</template>

<!----------------------------------------------->
<!--                    SCRIPT                 -->
<!----------------------------------------------->

<script scoped>
export default {
  /* Name */
  name: "NameHere",
  /* Data */
  data() {
    return {};
  },
  /* Components */
  components: {},
  /* Props */
  props: {},
  /* Methods */
  methods: {
    methodName(methodParam) {
      /* Here method logic */
    },
  },
  /* Computed */
  computed: {
    showVolver() {
      if (this.$route.path === "/") {
        return false;
      } else {
        return true;
      }
    },
    showAbout() {
      if (this.$route.path === "/about") {
        return false;
      } else {
        return true;
      }
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
p {
  margin: 0.5em;
  color: white;
  margin-left: 1em;
}

.footer {
  background-color: #0f0a31;
  margin-top: 2em;
  bottom: 0;
  width: 120%;
  position: fixed;
  margin-bottom: 0.01em;
  z-index: 999;
}
</style>
