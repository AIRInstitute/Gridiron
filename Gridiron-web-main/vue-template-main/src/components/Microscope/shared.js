import Navbar from "../../components/Partials/Navbar";
import NavbarMobile from "../../components/Partials/NavbarMobile";
import SocketioService from "../../services/socketio.service";

var MyShared = {
    /* Name */
    name: "DesktopInvetory",
    /* Data */
    data() {
        return {
            NoLiquid: "",
            Liquid: "",
            cellsNumber: -1,
            cellsAliveNumber: 0,
            cellsDeadNumber: 0
        };
    },
    /* Components */
    components: {
        Navbar,
        NavbarMobile
    },
    created() {
        SocketioService.setupSocketConnection();

    },
    beforeUnmount() {
        SocketioService.disconnect();
    },
    /* Props */
    props: {},
    /* Methods */
    methods: {
        async getImageNoLiquid() {

            // Diable de buttons while waiting for the protocol to
            var buttons = document.getElementsByClassName("btn profile-button")
            buttons[1].hidden = true
            buttons[2].hidden = true
            buttons[0].hidden = true

            var spinners = document.getElementsByClassName("fas fa-spinner fa-spin")
            spinners[0].hidden = false
            spinners[1].hidden = false
            /*
            var canvas = document.getElementById("Liquid");
            canvas.hidden = true
            document.getElementById("LiquidButton").hidden = true
            */
            this.Liquid = ""
            document.getElementById("microscopeResults2").hidden = true
            document.getElementById("goToP1").hidden = true

            //------------------------------------------
            // TODO: Microscope call to get photo
            //------------------------------------------

            //var url_flask = "http://192.168.2.233:5000/microscope/getAnImage"
            var url = process.env.VUE_APP_GET_IMAGE_WITHOUT_LIQUID;
            var xhr = new XMLHttpRequest();
            xhr.open("POST", url, true);
            xhr.setRequestHeader("Content-Type", "application/json");
            xhr.send(JSON.stringify({
                value: url
            }));
            SocketioService.socket.on("predictionWithoutLiquid", (msg) => {
                //console.log("Ahora viene sin liquido ");
                //console.log("msg: ", msg);
                var img_array_show = JSON.parse(msg["image"]);
                this.cellsNumber = msg["totalNumberOfCells"];
                
                console.log(this.cellsNumber);

                console.log("img_array: ", img_array_show);
                
                var canvasNoLiquid = document.getElementById("noLiquid");
                canvasNoLiquid.hidden = false


                canvasNoLiquid.height = img_array_show.length;
                canvasNoLiquid.width = img_array_show[0].length;

                // Now that we have canvas to work with, we need to draw the image data into it:
                var ctx = canvasNoLiquid.getContext("2d");
                ctx.clearRect(0, 0, canvasNoLiquid.width, canvasNoLiquid.height);

                for (var i = 0; i < img_array_show.length; i++) {
                    for (var j = 0; j < img_array_show[0].length; j++) {
                        ctx.fillStyle = "rgb(" + img_array_show[i][j][0] + "," + img_array_show[i][j][1] + "," + img_array_show[i][j][2] + ")";
                        ctx.fillRect(i * 1, j * 1, 1, 1);
                    }
                }
                this.NoLiquid = this.Global_noLiquid
                document.getElementById("microscopeResults1").hidden = false
                document.getElementById("LiquidButton").hidden = false

                buttons[1].hidden = false
                buttons[2].hidden = false
                buttons[0].hidden = false

                spinners[0].hidden = true
                spinners[1].hidden = true

                //----------------------
                //Transform array to png
                // ----------------------
                //let img_array_show = JSON.parse(img_array)
                //console.log(img_array_show)

            })
            /*
            
            //--------------------
            // Request to AI back
            //--------------------

            var url ="http://192.168.2.233:5001/backendAI/processImageWithoutLiquid" 
            var json_array = {"array":img_array}
            
            var requestOptions = {
                method: 'POST',
                body: JSON.stringify(json_array),
                redirect: 'follow',
                headers:{
                    'Access-Control-Allow-Headers':'Content-Type', 
                    'Content-type':'application/json'
                }
            };
            
            const result = await fetch(url, requestOptions)
              .then(response => response.text())
              .then(result => this.cellsNumber=result)
              .catch(error => console.log('error', error));

            console.log(this.cellsNumber);
            
            //------------------------
            // this.NoLiquid = this.Global_noLiquid
            document.getElementById("microscopeResults1").hidden = false
            document.getElementById("LiquidButton").hidden = false

            buttons[1].hidden = false
            buttons[2].hidden = false
            buttons[0].hidden = false
            
            spinners[0].hidden = true
            spinners[1].hidden = true

            
            // const r = await fetch(url_flask)
            //  .then(response => response.text())
            //  .then(result => img_array = JSON.parse(result))
            //  .catch(error => console.log('error', error));

            //----------------------
            //Transform array to png
            // ----------------------
            //let img_array_show = JSON.parse(img_array)
            //console.log(img_array_show)

            */

        },

        async getImageLiquid() {

            var buttons = document.getElementsByClassName("btn profile-button")
            buttons[1].hidden = true
            buttons[2].hidden = true
            buttons[0].hidden = true

            var spinners = document.getElementsByClassName("fas fa-spinner fa-spin")
            spinners[0].hidden = false
            spinners[1].hidden = false

            //------------------------------------------
            // TODO: Microscope call to get photo
            //------------------------------------------
            
            var xhr = new XMLHttpRequest();
            xhr.open("POST", process.env.VUE_APP_GET_IMAGE_WITH_LIQUID);
            xhr.setRequestHeader("Content-Type", "application/json");
            xhr.send(JSON.stringify({
                'totalNumberOfCells': this.cellsNumber
            }));
            //var url_flask = "http://192.168.2.233:5000/microscope/getAnImage"
            //var img_array
            SocketioService.socket.on("predictionWithLiquid", (msg) => {

                //console.log("Ahora viene con liquido ");
                //console.log("msg: ", msg);
                var img_array_show_l = JSON.parse(msg["image"]);
                this.cellsNumber = msg["totalNumberOfCells"];
                this.cellsAliveNumber = msg["numberOfLifeCells"];
                this.cellsDeadNumber = msg["cellViability"];
                //console.log("img_array: ", img_array_show_l);

                var canvasLiquid = document.getElementsByName("Liquid");
                canvasLiquid.hidden = false

                canvasLiquid.height = img_array_show_l.length;
                canvasLiquid.width = img_array_show_l[0].length;

                // Now that we have canvas to work with, we need to draw the image data into it:
                var ctx_l = canvasLiquid.getContext("2d");
                ctx_l.clearRect(0, 0, canvasLiquid.width, canvasLiquid.height);

                for (var i = 0; i < img_array_show_l.length; i++) {
                    for (var j = 0; j < img_array_show_l[0].length; j++) {
                        ctx_l.fillStyle = "rgb(" + img_array_show_l[i][j][0] + "," + img_array_show_l[i][j][1] + "," + img_array_show_l[i][j][2] + ")";
                        ctx_l.fillRect(i * 1, j * 1, 1, 1);
                    }
                }

                document.getElementById("microscopeResults2").hidden = false
                document.getElementById("goToP1").hidden = false

                buttons[1].hidden = false
                buttons[2].hidden = false
                buttons[0].hidden = false

                spinners[0].hidden = true
                spinners[1].hidden = true

            })
            /*
            const r = await fetch(url_flask)
                .then(response => response.text())
                .then(result => img_array = JSON.parse(result))
                .catch(error => console.log('error', error));
            */
            //------------------------
            // Show Image
            //-----------------------

            /*let img_array_show = JSON.parse(img_array)
            console.log(img_array_show)

            var canvas = document.getElementById("Liquid");
            canvas.hidden = false

            canvas.height = img_array_show.length;
            canvas.width = img_array_show[0].length;

            // Now that we have canvas to work with, we need to draw the image data into it:
            var ctx = canvas.getContext("2d");
            ctx.clearRect(0, 0, canvas.width, canvas.height);

            for (var i = 0; i < img_array_show.length; i++) {
                for (var j = 0; j < img_array_show[0].length; j++) {
                    ctx.fillStyle = "rgb(" + img_array_show[i][j][0] + "," + img_array_show[i][j][1] + "," + img_array_show[i][j][2] + ")";
                    ctx.fillRect(i * 1, j * 1, 1, 1);
                }
            }*/

            //--------------------
            // Request to AI back
            //--------------------
            //var url = "http://192.168.2.233:5001/backendAI/processImageWithLiquid"

            /*var json_array = { "array": img_array }

            var requestOptions = {
                method: 'POST',
                body: JSON.stringify(json_array),
                redirect: 'follow',
                headers: {
                    'Access-Control-Allow-Headers': 'Content-Type',
                    'Content-type': 'application/json',
                    'totalNumberOfCells': this.cellsNumber
                }
            };
           
            /*
            const res = await fetch(url, requestOptions)
                .then(response => response.text())
                .then(result =>
                    result_liquid = result,
                )
                .catch(error => console.log('error', error));
            */
            //------------------------
            /*
            result_liquid = JSON.parse(result_liquid)
            this.Liquid = this.Global_Liquid
            this.cellsAliveNumber = result_liquid["numberOfLifeCells"]
            this.cellsDeadNumber = result_liquid["cellViability"]
            */

        }
    },
    async mounted() { },


};
export default MyShared;