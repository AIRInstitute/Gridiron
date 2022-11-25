import Navbar from "../../components/Partials/Navbar";
import NavbarMobile from "../../components/Partials/NavbarMobile";
import SocketioService from "../../services/socketio.service";

var MyShared = {
    /* Name */
    name: "DesktopInvetory",
    /* Data */
    data() {
        return {
            protocol: 0,
            falcon_array: ['A1'],
            falcon_tags: ['A1', 'A2', 'B1', 'B2', 'C1', 'C2', 'A3', 'A4', 'B3', 'B4'],
            eppendorfs_num: "",
            well_rack: 0,
            falcon_n: "",
            starting_volume: "",
            falcon_volumes: [],
        };
    },
    /* Components */
    components: {
        Navbar,
        NavbarMobile
    },
    /*
    created() {
        SocketioService.setupSocketConnection();

    },
    beforeUnmount() {
        SocketioService.disconnect(); 
    },*/
    /* Props */
    props: {},
    /* Methods */
    methods: {
        changeFalcons(number) {
            this.falcon_array = [];
            if (number > 10)
                this.falcon_n = 10

            for (let i = 0; i < this.falcon_n; i++) {
                this.falcon_array.push('A')
            }
        },
        changeProtocol(num) {
            this.protocol = num;
            for (let i = 0; i < 5; i++) {
                document.getElementById('p' + i).classList.remove('active')
            }
            document.getElementById('p' + num).classList.add('active')
            this.platewells_num = this.eppendorfs_num
            this.checkMod(this.eppendorfs_num);
        },
        checkMod(num) {
            if (num % 6 != 0) {
                this.well_rack = Math.trunc((num / 6)) + 1
            } else
                this.well_rack = (num / 6)
        },
        //-----------------------------------------------------------------------------------------------------
        // Protocol start
        //-----------------------------------------------------------------------------------------------------

        // Cambiar URL a la que se va a hacer el POST 

        startP1(falcon_num, eppendorfs_num, starting_volume) {
            //var url ="http://212.128.140.209:8000/execute_first_protocol"

            let falcon_values = []
            for (let i = 0; i < falcon_num; i++) {
                falcon_values.push(document.getElementById('f' + i).value);
            }

            let value = {
                "n_falcons_15ml": falcon_num,
                "n_eppendorfs": eppendorfs_num,
                "starting_v_falcon": starting_volume,
                "volume_falcons": falcon_values,
                "protocol": "protocol_1"
            }
            console.log(value)
            var xhr = new XMLHttpRequest();
            xhr.open("POST", process.env.VUE_APP_FIRST_PROTOCOL, true);
            xhr.setRequestHeader('Content-Type', 'application/json');
            // xhr.setRequestHeader('Access-Control-Allow-Origin','Content-Type')
            xhr.send(JSON.stringify({
                value
            }));

            // Diable de buttons while waiting for the protocol to
            var buttons = document.getElementsByClassName("btn profile-button")
            buttons[0].hidden = true

            var spinners = document.getElementsByClassName("fas fa-spinner fa-spin")
            spinners[0].hidden = false

            document.getElementById("selectionProtocol").hidden = true
            document.getElementById("waitForProtocol").hidden = false

            // Wait for the protocol to finish
            /*
            SocketioService.socket.on("resultPipette", (msg) => {
                var data = JSON.parse(msg);
                console.log(data);
                
                var buttons = document.getElementsByClassName("btn profile-button")
                buttons[0].hidden = false

                var spinners = document.getElementsByClassName("fas fa-spinner fa-spin")
                spinners[0].hidden = true

                document.getElementById("selectionProtocol").hidden = false
                document.getElementById("waitForProtocol").hidden = true
            });*/

            xhr.onreadystatechange = function () {
                if (this.readyState != 4) return;
                if (this.status == 200) {
                    //alert("Protocol finnished successfully");
                    var data = this.response;
                    console.log(data);
                    if (data["error"]) {
                        alert("Can't resolve protocol");
                        location.reload();
                    }
                    else {

                        alert("Protocol end succes");
                        var buttons = document.getElementsByClassName("btn profile-button")
                        buttons[0].hidden = false

                        var spinners = document.getElementsByClassName("fas fa-spinner fa-spin")
                        spinners[0].hidden = true

                        document.getElementById("selectionProtocol").hidden = false
                        document.getElementById("waitForProtocol").hidden = true
                    }
                }
            };


        },

        //--------------------------------------------------------------------------

        startP2(eppendorfs_num, volume) {

            //var url ="http://212.128.140.209:8081/execute_first_protocol"

            let value = {
                "n_eppendorfs": eppendorfs_num,
                "starting_v_falcon_B4": volume,
                "protocol": "protocol_2"
            }

            var xhr = new XMLHttpRequest();
            xhr.open("POST", process.env.VUE_APP_SECOND_PROTOCOL, true);
            xhr.setRequestHeader('Content-Type', 'application/json');
            //xhr.setRequestHeader('Access-Control-Allow-Origin', 'Content-Type')
            xhr.send(JSON.stringify({
                value: value
            }));

            // Diable de buttons while waiting for the protocol to
            var buttons = document.getElementsByClassName("btn profile-button")
            buttons[0].hidden = true

            var spinners = document.getElementsByClassName("fas fa-spinner fa-spin")
            spinners[0].hidden = false

            document.getElementById("selectionProtocol").hidden = true
            document.getElementById("waitForProtocol").hidden = false
            /*
            SocketioService.socket.on("resultPipette", (msg) => {
                var data = JSON.parse(msg);
                console.log(data);

                var buttons = document.getElementsByClassName("btn profile-button")
                buttons[0].hidden = false

                var spinners = document.getElementsByClassName("fas fa-spinner fa-spin")
                spinners[0].hidden = true

                document.getElementById("selectionProtocol").hidden = false
                document.getElementById("waitForProtocol").hidden = true
            });*/


            xhr.onreadystatechange = function () {
                if (this.readyState != 4) return;
                if (this.status == 200) {
                    var data = this.response;
                    console.log(data);
                    if (data["error"]) {
                        alert("Can't resolve protocol");
                        location.reload();
                    }
                    else {
                        alert("Protocol finnished successfully");

                        var buttons = document.getElementsByClassName("btn profile-button")
                        buttons[0].hidden = false

                        var spinners = document.getElementsByClassName("fas fa-spinner fa-spin")
                        spinners[0].hidden = true

                        document.getElementById("selectionProtocol").hidden = false
                        document.getElementById("waitForProtocol").hidden = true
                    }


                }

                if (this.status == 500) {
                    alert("Can't resolve protocol");
                    console.log("can't resolve")
                    return;
                }
            };
        },

        //--------------------------------------------------------------------------

        startP3(eppendorfs_num, falcon_num, well_rack) {

            //var url ="http://212.128.140.209:8081/start_protocol"


            let value = {
                "n_eppendorfs": eppendorfs_num,
                "n_falcons_50ml": falcon_num,
                "n_wellplates": well_rack,
                "protocol": "protocol_3"
            }

            var xhr = new XMLHttpRequest();
            xhr.open("POST", process.env.VUE_APP_THIRD_PROTOCOL, true);
            xhr.setRequestHeader('Content-Type', 'application/json');
            //xhr.setRequestHeader('Access-Control-Allow-Origin', 'Content-Type')
            xhr.send(JSON.stringify({
                value: value
            }));

            // Diable de buttons while waiting for the protocol to
            var buttons = document.getElementsByClassName("btn profile-button")
            buttons[0].hidden = true

            var spinners = document.getElementsByClassName("fas fa-spinner fa-spin")
            spinners[0].hidden = false

            document.getElementById("selectionProtocol").hidden = true
            document.getElementById("waitForProtocol").hidden = false
            /*
            SocketioService.socket.on("resultPipette", (msg) => {
                var data = JSON.parse(msg);
                console.log(data);
                
                var buttons = document.getElementsByClassName("btn profile-button")
                buttons[0].hidden = false

                var spinners = document.getElementsByClassName("fas fa-spinner fa-spin")
                spinners[0].hidden = true

                document.getElementById("selectionProtocol").hidden = false
                document.getElementById("waitForProtocol").hidden = true
            });
            */
            xhr.onreadystatechange = function () {
                if (this.readyState != 4) return;
                if (this.status == 200) {
                    var data = this.response;
                    console.log(data);
                    if (data["error"]) {
                        alert("Can't resolve the protocol")
                        location.reload();
                    }
                    else {
                        alert("Protocol finnished successfully");

                        var buttons = document.getElementsByClassName("btn profile-button")
                        buttons[0].hidden = false

                        var spinners = document.getElementsByClassName("fas fa-spinner fa-spin")
                        spinners[0].hidden = true

                        document.getElementById("selectionProtocol").hidden = false
                        document.getElementById("waitForProtocol").hidden = true
                    }


                }

                if (this.status == 500) {
                    alert("Can't resolve protocol");
                    console.log("can't resolve")
                    return;
                }
            };
        },

        //--------------------------------------------------------------------------

        startP4(cuvette_num) {

            //var url ="http://212.128.140.209:8081/start_protocol"

            let value = {
                "n_eppendorfs": cuvette_num,
                "protocol": "protocol_4"
            }

            var xhr = new XMLHttpRequest();
            xhr.open("POST", process.env.VUE_APP_FOURTH_PROTOCOL, true);
            xhr.setRequestHeader('Content-Type', 'application/json');
            //xhr.setRequestHeader('Access-Control-Allow-Origin', 'Content-Type')
            xhr.send(JSON.stringify({
                value: value
            }));

            // Diable de buttons while waiting for the protocol to
            var buttons = document.getElementsByClassName("btn profile-button")
            buttons[0].hidden = true

            var spinners = document.getElementsByClassName("fas fa-spinner fa-spin")
            spinners[0].hidden = false

            document.getElementById("selectionProtocol").hidden = true
            document.getElementById("waitForProtocol").hidden = false
            /*
            SocketioService.socket.on("resultPipette", (msg) => {
                var data = JSON.parse(msg);
                console.log(data);
                
                var buttons = document.getElementsByClassName("btn profile-button")
                buttons[0].hidden = false

                var spinners = document.getElementsByClassName("fas fa-spinner fa-spin")
                spinners[0].hidden = true

                document.getElementById("selectionProtocol").hidden = false
                document.getElementById("waitForProtocol").hidden = true
            });
            */
            xhr.onreadystatechange = function () {
                if (this.readyState != 4) return;
                if (this.status == 200) {
                    var data = this.response;
                    console.log(data);
                    if (data["error"]) {
                        alert("Can't resolve the protocol");
                        location.reload();
                    } else {
                        alert("Protocol finnished successfully");

                        var buttons = document.getElementsByClassName("btn profile-button")
                        buttons[0].hidden = false

                        var spinners = document.getElementsByClassName("fas fa-spinner fa-spin")
                        spinners[0].hidden = true

                        document.getElementById("selectionProtocol").hidden = false
                        document.getElementById("waitForProtocol").hidden = true
                    }


                }
            };
        },

        //--------------------------------------------------------------------------

        startP5(cuvette_num, well_rack) {
            //var url ="http://212.128.155.117:8081/start_protocol"

            console.log(cuvette_num, well_rack);
            let value = {
                "n_cuvettes": cuvette_num,
                "n_wellplates": well_rack,
                "protocol": "protocol_5"
            }
            console.log("Pre llamada");
            var xhr = new XMLHttpRequest();
            xhr.open("POST", process.env.VUE_APP_FIFTH_PROTOCOL, true);
            xhr.setRequestHeader('Content-Type', 'application/json');
            //xhr.setRequestHeader('Access-Control-Allow-Origin', 'Content-Type')
            xhr.send(JSON.stringify({
                value: value
            }));
            console.log("post llamada");

            // Disable de buttons while waiting for the protocol to
            var buttons = document.getElementsByClassName("btn profile-button")
            buttons[0].hidden = true

            var spinners = document.getElementsByClassName("fas fa-spinner fa-spin")
            spinners[0].hidden = false

            document.getElementById("selectionProtocol").hidden = true
            document.getElementById("waitForProtocol").hidden = false
            /*
            SocketioService.socket.on("resultPipette", (msg) => {
                var data = JSON.parse(msg);
                console.log(data);

                var buttons = document.getElementsByClassName("btn profile-button")
                buttons[0].hidden = false

                var spinners = document.getElementsByClassName("fas fa-spinner fa-spin")
                spinners[0].hidden = true

                document.getElementById("selectionProtocol").hidden = false
                document.getElementById("waitForProtocol").hidden = true
            });
            */
            xhr.onreadystatechange = function () {
                if (this.readyState != 4) return;
                if (this.status == 200) {
                    var data = this.response;
                    console.log(data);
                    if (data["error"]) {
                        alert("Can't resolve protocol");
                        location.reload();
                    } else {
                        alert("Protocol finnished successfully");
                        var data = JSON.parse(this.responseText);
                        console.log(data);

                        var buttons = document.getElementsByClassName("btn profile-button")
                        buttons[0].hidden = false

                        var spinners = document.getElementsByClassName("fas fa-spinner fa-spin")
                        spinners[0].hidden = true

                        document.getElementById("selectionProtocol").hidden = false
                        document.getElementById("waitForProtocol").hidden = true
                    }


                }
            };
        },

        //--------------------------------------------------------------------------

        startP6() {
            //var url ="http://212.128.140.209:8081/start_protocol"

            let value = {
                "protocol": "protocol_6"
            }

            var xhr = new XMLHttpRequest();
            xhr.open("POST", process.env.VUE_APP_START_PROTOCOL, true);
            xhr.setRequestHeader('Content-Type', 'application/json');
            //xhr.setRequestHeader('Access-Control-Allow-Origin', 'Content-Type')
            xhr.send(JSON.stringify({
                value: value
            }));

            // Diable de buttons while waiting for the protocol to
            var buttons = document.getElementsByClassName("btn profile-button")
            buttons[0].hidden = true

            var spinners = document.getElementsByClassName("fas fa-spinner fa-spin")
            spinners[0].hidden = false

            document.getElementById("selectionProtocol").hidden = true
            document.getElementById("waitForProtocol").hidden = false
            /*
            SocketioService.socket.on("resultPipette", (msg) => {
                var data = JSON.parse(msg);
                console.log(data);

                var buttons = document.getElementsByClassName("btn profile-button")
                buttons[0].hidden = false

                var spinners = document.getElementsByClassName("fas fa-spinner fa-spin")
                spinners[0].hidden = true

                document.getElementById("selectionProtocol").hidden = false
                document.getElementById("waitForProtocol").hidden = true
            });
            */

            xhr.onreadystatechange = function () {
                if (this.readyState != 4) return;
                if (this.status == 200) {
                    var data = this.response;
                    console.log(data);
                    if (data["error"]) {
                        alert("Can't resolve protocol");
                        location.reload();
                    } else {
                        alert("Protocol finnished successfully");
                        var buttons = document.getElementsByClassName("btn profile-button")
                        buttons[0].hidden = false

                        var spinners = document.getElementsByClassName("fas fa-spinner fa-spin")
                        spinners[0].hidden = true

                        document.getElementById("selectionProtocol").hidden = false
                        document.getElementById("waitForProtocol").hidden = true
                    }
                }
            };
        }

    },
    async mounted() { },

};
export default MyShared;