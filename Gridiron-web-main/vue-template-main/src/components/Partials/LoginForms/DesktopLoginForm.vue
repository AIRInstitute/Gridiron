<!----------------------------------------------->
<!--                  TEMPLATE                 -->
<!----------------------------------------------->
<template>
  <div
    class="row formulario justify-content-center animation a1"
    style="width: 100%"

  >
    <div class="form-signin login justify-content-center">
      <!--
      <img
        class="logo"
        v-bind:src="projectLogo"
        alt="logo"
      /> -->
      <h2 class="animation a1"><strong>Sign In</strong></h2>
      <h3 class="animation a2">Introduce your email and password</h3>
      <form class="animation a3">
        <div class="form-group">
          <input type="email" class="form-control" placeholder="Enter email" v-model="username"/>
        </div>
        <div class="form-group">
          <input type="password" class="form-control" placeholder="Password" v-model="pass" />
        </div>
      </form>
      <div class="row justify-content-center btn-row">
        <button class="btn animation a4" @click="onEnter(username,pass)" style="color:white" :style="'background-color:'+ primaryColor" >
          Sign In
        </button>
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
.form-signin{
  z-index: 999;
}
.logo{
  height: 10em;
  filter:  brightness(0) invert(0);
  margin-bottom: 1em;
}
.btn {
  background-color: rgb(255, 255, 255);
}
h1 {
  color: black;
}

.login {
  overflow: hidden;
  padding: 40px 30px 30px 30px;
  width: 45em;
  margin-top: 16em;
}
@media (max-width: 600px) {

  .login {
    margin: auto;
    overflow: hidden;
    width: 100%;
    margin-top: 2em;
    margin-bottom: 2em;
  }
}
.login > .row > button {
  cursor: pointer;
  color: rgb(255, 255, 255);
  font-size: 16px;
  width: 80px;
  border: 0;
  padding: 10px 0;
  margin-left: -5px;
  border-radius: 5px;
  background-color: #cf8fa2;
}

.login > button:hover {
  background-color: rgb(196, 196, 196);
}

h2 {
  margin: 0;
  color: #000000;
}
h3 {
  margin-top: 10px;
  font-weight: normal;
  font-size: 18px;
  color: rgb(0, 0, 0);
}

.animation {
  animation-name: move;
  animation-duration: 0.4s;
  animation-fill-mode: both;
  animation-delay: 0s;
}

.remember-check {
  color: black;
}

.a1 {
  animation-delay: 0.5s;
}

.a2 {
  animation-delay: 0.6s;
}

.a3 {
  animation-delay: 0.7s;
}

.a4 {
  animation-delay: 0.8s;
}

.a5 {
  animation-delay: 0.9s;
}

.a6 {
  animation-delay: 1s;
}

.a7 {
  animation-delay: 1.1s;
}

@keyframes move {
  0% {
    opacity: 0;
    visibility: hidden;
    transform: translateY(-40px);
  }

  100% {
    opacity: 1;
    visibility: visible;
    transform: translateY(0);
  }
}

@keyframes left {
  0% {
    opacity: 0;
    width: 0;
  }

  100% {
    opacity: 1;
    padding: 20px 40px;
    width: 440px;
  }
}
</style>
