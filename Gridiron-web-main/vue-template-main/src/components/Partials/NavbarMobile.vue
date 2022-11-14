<!----------------------------------------------->
<!--                  TEMPLATE                 -->
<!----------------------------------------------->
<template>
  <!-- Nav -->
  <nav class="navbar navbar-expand-lg navbar-light bg-light" :style="'font-family:'+ primaryFont">
    <a class="navbar-brand">
      <router-link to="/">
        <img
          class="nav-bar-logo"
          v-bind:src="projectLogo"
          alt="logo"
        />
      </router-link>
    </a>

      <div class="d-flex align-items-center">
          <li class="nav-item dropdown">
            <a
              class="nav-link dropdown-toggle"
              id="navbarDropdown"
              role="button"
              data-toggle="dropdown"
              aria-haspopup="false"
              aria-expanded="false"
              style="padding-top: 0.5em"
            >
              <i class="fas fa-bell notifications"></i>
                {{user.name}}
            </a>
            <div class="dropdown-menu" aria-labelledby="navbarDropdown">
              <a class="dropdown-item" @click="goUserProfile(user.id)">Go to profile</a>
              <a class="dropdown-item" @click="logout()">Close session</a>
              <div class="dropdown-divider"></div>
              <a class="dropdown-item" v-for="i in 4" :key="i">
                <i class="fas fa-bell notifications"></i> Notificacion 1
              </a>
            </div>
          </li>
          <li class="nav-item">
            <img
              :src="user.picture_url"
              class="rounded-circle"
              height="50"
              alt=""
              width="50"
              @click="$refs.profileModal.openModal()"
            />
          </li>
      </div>
  </nav>
</template>

<!----------------------------------------------->
<!--                    SCRIPT                 -->
<!----------------------------------------------->

<script>
var $ = require("jquery");
var dt = require("datatables.net");
import MyShared from "./sharedNavBar";

export default {
  mixins: [MyShared],
};
</script>
<!----------------------------------------------->
<!--                    STYLES                 -->
<!----------------------------------------------->
<style scoped>
li {
    list-style-type: none;
}
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
  font-size: 1.2em;
}
.dropdown-menu {
  margin-top: 2em;
  position: absolute !important;
}
</style>
