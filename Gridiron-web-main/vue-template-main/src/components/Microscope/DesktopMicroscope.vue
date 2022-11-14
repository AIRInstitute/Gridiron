<!----------------------------------------------->
<!--                  TEMPLATE                 -->
<!----------------------------------------------->
<template>
<div class="aux">
    <Navbar></Navbar>
    <div class="maincontainer" :style="'--my-font-var:' + primaryFont + ';'" style="text-align:center">
        <div class="container">
            <div class="row">
                 <!-- ------------------------------------- Description ------------------------------------- -->
                <div class="col-4">
                    <h3 class="mt-3">Microscope description</h3>
                    <hr> 
                    <div style="text-align:left">
                        Microscope description about what the microscope does, so that I print a description about what the microscope does,
                        but not printing a description about what a microscope is or how it looks like cause it will be unnecessary
                    </div>
                     <div id="microscopeResults1" hidden>
                        <hr>
                        <div class="col-md-12"><label class="labels">Total number of cells</label></div>
                        <label for="sd">{{cellsNumber}}</label>
                    </div>
                    <div id="microscopeResults2" hidden>
                        <div class="col-md-12"><label class="labels">Number of alive cells</label></div>
                        <label for="sd">{{cellsAliveNumber}}</label>
                        <div class="col-md-12"><label class="labels">Cell Viability</label></div>
                        <label for="sd">{{cellsDeadNumber}}</label>
                    </div>
                    <div  id="goToP1" class="mt-5 text-center" hidden>
                            <a class="btn profile-button" href='#/protocols'  type="button" style="margin-top:-8px" :style="'background-color:'+primaryColor">Go to Protocol 1</a>
                    </div>
                </div>
                <!-- ------------------------------------- No Liquid Image ------------------------------------- -->
                <div class="col-4">
                    <h3 class="mt-3">Image without Trypan Blue</h3>
                    <hr>
                        <div class="row mt-2" id="el_div">
                            <canvas id="noLiquid" >
                            </canvas>
                            
                        </div>
                    <div class="mt-5 text-center">
                        <button id = "nL" class="btn profile-button" type="button" :style="'background-color:'+primaryColor" @click="getImageNoLiquid()">Get New Image</button>
                        <i  class="fas fa-spinner fa-spin" hidden></i>
                    </div>
                </div>
                <!-- ---------------------------------------  Liquid Image ------------------------------------- -->
                <div class="col-4">
                    <h3 class="mt-3">Image with Trypan Blue</h3>
                    <hr>
                   <div class="row mt-2" id="el_div">
                            <canvas id="Liquid" name = "Liquid" >
                            </canvas>
                            
                        </div>
                    <div id="LiquidButton" class="mt-5 text-center" hidden>
                        <a id = "nL" class="btn profile-button" type="button" :style="'background-color:'+primaryColor" @click="getImageLiquid()">Get New Image</a>
                        <i  class="fas fa-spinner fa-spin" hidden></i>
                    </div>
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
    font-weight: 600;
    font-size: 15px
}
.label-info{
    font-weight: 300;
    font-size: 15px;
    margin-top: -5px !important;
}
.btn{
    color: white;
    box-shadow: none;

}

.maincontainer{
    padding-bottom: 4em;
}
</style>


