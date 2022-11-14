<!----------------------------------------------->
<!--                  TEMPLATE                 -->
<!----------------------------------------------->
<template>
  <NavbarMobile></NavbarMobile>
  <div class="maincontainer" :style="'--my-font-var:' + primaryFont + ';'">
    <div class="container">
        <div class="row">
            <div class="col-md-3 border-right">
                <div class="d-flex flex-column align-items-center text-center p-3 py-5"><img class="rounded-circle mt-5" style="width:150px; height:150px" :src="user.picture_url"><span class="font-weight-bold">{{user.name}}</span><span class="text-black-50">{{user.email}}</span><span> </span></div>
            </div>
            <div class="col-md-8 border-right">
                <div class="p-3 pb-5">
                    <div class="d-flex justify-content-between align-items-center mb-3">
                        <h4 class="text-right">Profile Settings</h4>
                    </div>
                    <div class="row mt-2">
                        <div class="col-md-6"><label class="labels">Name</label><input type="text" class="form-control" :style="'--my-color-var:' + primaryColor + ';'" placeholder="first name" :value="user.name"></div>
                        <div class="col-md-6"><label class="labels">Surname</label><input type="text" class="form-control" :style="'--my-color-var:' + primaryColor + ';'" :value="user.surname" placeholder="surname"></div>
                    </div>
                    <div class="row mt-3">
                        <div class="col-md-12"><label class="labels">Mobile Number</label><input type="text" class="form-control" :style="'--my-color-var:' + primaryColor + ';'" placeholder="enter phone number" :value="user.phone"></div>
                        <div class="col-md-12"><label class="labels">Email</label><input type="text" class="form-control" :style="'--my-color-var:' + primaryColor + ';'" placeholder="enter email id" :value="user.email"></div>
                    </div>
                    <div class="row mt-3">
                        <div class="col-md-6"><label class="labels">New Password</label><input type="password" class="form-control" :style="'--my-color-var:' + primaryColor + ';'" placeholder="" value=""></div>
                        <div class="col-md-6"><label class="labels">Repeat New Password</label><input type="password" class="form-control" :style="'--my-color-var:' + primaryColor + ';'" value="" placeholder=""></div>
                    </div>
                    <div class="row mt-3">
                        <div class="col-md-6"><label class="labels">Country</label><input type="text" class="form-control" :style="'--my-color-var:' + primaryColor + ';'" placeholder="country" :value="user.country"></div>
                        <div class="col-md-6"><label class="labels">State/Region</label><input type="text" class="form-control" :style="'--my-color-var:' + primaryColor + ';'" :value="user.state" placeholder="state"></div>
                    </div>
                    <div class="mt-5 text-center"><button class="btn profile-button" type="button" :style="'background-color:'+primaryColor">Save Profile</button></div>
                </div>
            </div>
        </div>
    </div>
  </div>
</template>

<!----------------------------------------------->
<!--                    SCRIPT                 -->
<!----------------------------------------------->
<script>
import MyShared from './shared';

export default{
    mixins:[MyShared],
}
</script>

<!----------------------------------------------->
<!--                    STYLES                 -->
<!----------------------------------------------->
<style scoped>
.maincontainer{
    font-family: var(--my-font-var);
}
a {
  text-decoration: none;
}

.form-control:focus {
    box-shadow: none;
    border-color: var(--my-color-var)
}
.labels {
    font-size: 11px
}

</style>



