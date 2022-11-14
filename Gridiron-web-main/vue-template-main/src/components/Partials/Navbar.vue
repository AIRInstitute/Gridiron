<!----------------------------------------------->
<!--                  TEMPLATE                 -->
<!----------------------------------------------->
<template>
  <!-- Nav -->
  <nav class="navbar navbar-expand-lg navbar-light bg-light" :style="'font-family:'+ primaryFont">
    <a class="navbar-brand">
      <router-link to="/dashboard">
        <img
          class="nav-bar-logo"
          v-bind:src="projectLogo"
          alt="logo"
        />
      </router-link>
    </a>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav mr-auto"></ul>
      <div class="form-inline my-2 my-lg-0">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item dropdown">
            <a
              class="nav-link dropdown-toggle"
              id="navbarDropdown"
              role="button"
              data-toggle="dropdown"
              aria-haspopup="false"
              aria-expanded="false"
              style="padding-top: 1em"
            >
              <i class="fas fa-user" style="padding-top:1m;margin-right:1em"></i>
              <a>{{user.name}}</a>              
            </a>
            <div class="dropdown-menu" aria-labelledby="navbarDropdown">
              <a class="dropdown-item" @click="goUserProfile(user.id)">Go to profile</a>
              <a class="dropdown-item" @click="logout()">Close session</a>
            </div>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<!----------------------------------------------->
<!--                    SCRIPT                 -->
<!----------------------------------------------->

<script>
var $ = require("jquery");
var dt = require("datatables.net");
import { useUserStore } from './user';
import MyShared from "./sharedNavBar";

export default { 
  mixins: [MyShared],
};
</script>
<!----------------------------------------------->
<!--                    STYLES                 -->
<!----------------------------------------------->
<style scoped>
.username {
  padding-bottom: 15%;
  padding-top: 15%;
  margin-right: 0.5em;
  height: 100%;
}
.nav-bar-logo {
  height: 2em;
}
.notifications {
  font-size: 1em;
  margin-right: 1em;
}
.dropdown-menu {
  position: absolute !important;
  margin-right:5em ;
}
.dropdown-toggle{
  margin-left:2em
}
</style>
