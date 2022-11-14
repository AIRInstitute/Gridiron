<!----------------------------------------------->
<!--                  TEMPLATE                 -->
<!----------------------------------------------->
<template>
<div class="aux">
    <Navbar></Navbar>
    <div class="maincontainer" :style="'--my-font-var:' + primaryFont + ';'">
        <div class="container">
            <div class="row">
                <div id="selectionProtocol" class="col-12 text-center protocols-div">
                    <div id="p0" class="btn active btn-protocol" @click="changeProtocol(0)">PROTOCOL 1</div>
                    <div id="p1" class="btn btn-protocol" @click="changeProtocol(1)">PROTOCOL 2</div>
                    <div id="p2" class="btn btn-protocol"  @click="changeProtocol(2)">PROTOCOL 3</div>
                    <div id="p3" class="btn btn-protocol" @click="changeProtocol(3)">PROTOCOL 4</div>
                    <div id="p4" class="btn btn-protocol" @click="changeProtocol(4)">PROTOCOL 5</div>
                    <div id="p4" class="btn btn-protocol" @click="changeProtocol(5)">PROTOCOL 6</div>
                </div>
                <div id="waitForProtocol" class="col-12 text-center protocols-div" hidden>
                    <div id="p0" class="btn active btn-protocol">Waiting for protocol to end</div>
                </div>
            </div>
            <div class="row">
                <!-- ------------------------------------- Protocol 1 ------------------------------------- -->
                <div class="col-6" v-if="protocol == 0">
                    <h3 class="mt-4">Protocol description</h3>
                    <hr> 
                    Process of aspiration from Falcon tubes 15ml and dispensation of n calculated ml into eppendorf tubes.
                </div>
                <div class="col-6" v-if="protocol == 0">
                    <h3 class="mt-4">Settings</h3>
                    <hr>
                    <div class="row mt-2">
                        <div class="col-md-12"><label class="labels">Number of Falcon Tubes</label><input type="number" class="form-control" :style="'--my-color-var:' + primaryColor + ';'" placeholder="Number of Falcon Tubes" v-model="falcon_n" @change="changeFalcons(falcon_n)"></div>
                    </div>
                    <div class="row mt-2 falcon-div">
                        <div class="col-md-6" v-for="(item, index) in falcon_array" :key="index"><label class="labels">Falcon {{falcon_tags[index]}}</label><input type="text" class="form-control" :style="'--my-color-var:' + primaryColor + ';'" :placeholder="'Falcon ' + falcon_tags[index]" :id="'f'+index"></div>
                    </div>
                    <div class="row mt-2">
                        <div class="col-md-12"><label class="labels">Number of Eppendorfs</label><input type="number" max=10 min=1 class="form-control" :style="'--my-color-var:' + primaryColor + ';'" placeholder="Number of Eppendorfs" v-model="eppendorfs_num"></div>
                    </div>
                    <div class="row mt-2">
                        <div class="col-md-12"><label class="labels">Starting Volume of Falcon Tubes in μL</label><input type="text" class="form-control" :style="'--my-color-var:' + primaryColor + ';'" placeholder="Starting Volume of Falcon Tubes in μL" v-model="starting_volume"></div>
                    </div>
                    <div class="mt-5 text-center">
                        <button class="btn profile-button" type="button" :style="'background-color:'+primaryColor" @click="startP1(falcon_array.length,eppendorfs_num,starting_volume)">Start Protocol</button>
                        <i  class="fas fa-spinner fa-spin" hidden></i>
                    </div>
                </div>
                <!-- ------------------------------------- Protocol 2 ------------------------------------- -->
                <div class="col-6" v-if="protocol == 1">
                    <h3 class="mt-4">Protocol description</h3>
                    <hr>
                    Process of aspiration from 1 Falcon tube 50ml with antibodies and dispensation in eppendorf tubes with cells
                </div>
                <div class="col-6" v-if="protocol == 1">
                    <h3 class="mt-4">Settings</h3>
                    <hr>
                    <div class="row mt-2">
                        <div class="col-md-12"><label class="labels">Number of Eppendorfs</label><input type="Number" class="form-control" :style="'--my-color-var:' + primaryColor + ';'" placeholder="Number of Eppendorfs" v-model="eppendorfs_num" min=1 max=24></div>
                    </div>
                    <div class="row mt-2">
                        <div class="col-md-12"><label class="labels">Volume of Falcon B4 Tube in μL</label><input type="text" class="form-control" :style="'--my-color-var:' + primaryColor + ';'" placeholder="Volume of Falcon B4 Tube in μL" v-model="volume"></div>
                    </div>
                    <div class="mt-5 text-center">
                        <button class="btn profile-button" type="button" :style="'background-color:'+primaryColor" @click="startP2(eppendorfs_num,volume)">Start Protocol</button>
                        <i  class="fas fa-spinner fa-spin" hidden></i>
                    </div>
                </div>
                <!-- ------------------------------------- Protocol 3 ------------------------------------- -->
                <div class="col-6" v-if="protocol == 2">
                    <h3 class="mt-4">Protocol description</h3>
                    <hr>
                    Process of aspiration from Falcon tubes 50ml and dispensation of 3 x 1ml into wellplates
                </div>
                <div class="col-6" v-if="protocol == 2">
                    <h3 class="mt-4">Settings</h3>
                    <hr>
                    <div class="row mt-2">
                        <div class="col-md-12"><label class="labels">Number of Wellplates</label><input type="text" class="form-control" :style="'--my-color-var:' + primaryColor + ';'" placeholder="Number of Eppendorfs" v-model="platewells_num" @change="checkMod(platewells_num)"></div>
                    </div>
                    <div class="row mt-0 pt-0">
                        <div class="col-md-12 pt-1"><label class="labels label-info">Number of wellplates racks necessary: {{well_rack}}</label></div>
                    </div>
                    <div class="row mt-2">
                        <div class="col-md-12"><label class="labels">Number of falcons</label><input type="text" class="form-control" :style="'--my-color-var:' + primaryColor + ';'" placeholder="Number of Falcons" v-model="falcon_num" ></div>
                    </div>
                    <div class="row mt-0 p-0">
                        <div class="col-md-12 pt-1"><label class="labels label-info">The falcons will be place A3, A4, B3 and will have 25ml of solution each.</label></div>
                    </div>
                    <div class="mt-5 text-center">
                        <button class="btn profile-button" type="button" :style="'background-color:'+primaryColor" @click="startP3(eppendorfs_num,falcon_num,well_rack)">Start Protocol</button>
                        <i  class="fas fa-spinner fa-spin" hidden></i>
                    </div>
                </div>
                <!-- ------------------------------------- Protocol 4 ------------------------------------- -->                
                <div class="col-6" v-if="protocol == 3">
                    <h3 class="mt-4">Protocol description</h3>
                    <hr>
                    Process of aspiration from eppendorf tubes and dispensation of 0.4ml of solution into custom cuvettes
                </div>
                <div class="col-6" v-if="protocol == 3">
                    <h3 class="mt-4">Settings</h3>
                    <hr>
                    <div class="row mt-2">
                        <div class="col-md-12"><label class="labels">Number of Cuvettes</label><input type="text" class="form-control" :style="'--my-color-var:' + primaryColor + ';'" placeholder="Number of Cuvettes" v-model="eppendorfs_num"></div>
                    </div>
                    <div class="mt-5 text-center">
                        <button class="btn profile-button" type="button" :style="'background-color:'+primaryColor" @click="startP4(eppendorfs_num)">Start Protocol</button>
                        <i  class="fas fa-spinner fa-spin" hidden></i>
                    </div>
                </div>
                <!-- ------------------------------------- Protocol 5 ------------------------------------- -->
                <div class="col-6" v-if="protocol == 4">
                    <h3 class="mt-4">Protocol description</h3>
                    <hr>
                    Process of aspiration from custom cuvettes with solution and dispensation into wellplates
                </div>
                <div class="col-6" v-if="protocol == 4">
                    <h3 class="mt-4">Settings</h3>
                    <hr>
                    <div class="row mt-2">
                        <div class="col-md-12"><label class="labels">Number of Cuvettes</label><input type="text" class="form-control" :style="'--my-color-var:' + primaryColor + ';'" placeholder="Number of Cuvettes" v-model="eppendorfs_num" @change="checkMod(eppendorfs_num)"></div>
                    </div>
                    <div class="row mt-0 pt-0">
                        <div class="col-md-12 pt-1"><label class="labels label-info">Number of wellplates necessary: {{eppendorfs_num}}</label></div>
                    </div>
                    <div class="row mt-0 pt-0">
                        <div class="col-md-12 pt-1"><label class="labels label-info">Number of wellplates racks necessary: {{well_rack}}</label></div>
                    </div>       
                    <div class="mt-5 text-center">
                        <button class="btn profile-button" type="button" :style="'background-color:'+primaryColor" @click="startP5(eppendorfs_num,well_rack)">Start Protocol</button>
                        <i class="fas fa-spinner fa-spin" hidden></i>
                    </div>             
                </div>
                <!-- ------------------------------------- Protocol 6 ------------------------------------- -->
                <div class="col-6" v-if="protocol == 5">
                    <h3 class="mt-4">Protocol description</h3>
                    <hr>
                    Second day protocol where cells are detached from the wellplates and placed into eppendorf tubes
                </div>
                <div class="col-6" v-if="protocol == 5">
                    <h3 class="mt-4">Settings</h3>
                    <hr>
                    <div class="row mt-2">
                        <div class="col-md-12"><label class="labels">No setttings necessary</label><input disabled type="text" class="form-control" :style="'--my-color-var:' + primaryColor + ';'" placeholder="" v-model="eppendorfs_num" @change="checkMod(eppendorfs_num)"></div>
                    </div>
                    <div class="mt-5 text-center">
                        <button class="btn profile-button" type="button" :style="'background-color:'+primaryColor" @click="startP6()">Start Protocol</button>
                        <i class="fas fa-spinner fa-spin" hidden></i>
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
.protocols-div{
    margin-top: 1em;
box-shadow: rgba(9, 30, 66, 0.25) 0px 4px 8px -2px, rgba(9, 30, 66, 0.08) 0px 0px 0px 1px;}
.active{
   color: #6caecf !important;
   border-bottom: solid 2px #6caecf;
}
.falcon-div{
    padding-left: 2em;
    padding-right: 2em;
    margin-left: 0.5em;
    margin-right: 0.5em;
    box-shadow: rgba(0, 0, 0, 0.075) 0px 0px 0px 1px;
}

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
.btn-protocol{
    color: black;
}
.maincontainer{
    padding-bottom: 4em;
}
</style>


