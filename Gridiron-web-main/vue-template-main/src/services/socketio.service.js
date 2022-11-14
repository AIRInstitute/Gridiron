const { io } = require("socket.io-client");

const socket = io();

class SocketIOService {
    socket;
    constructor() {
    }

    setupSocketConnection() {
        this.socket = io(process.env.VUE_APP_SOCKET_ENDPOINT);
        this.socket.on("connect", () => {
            console.log("Connected to socket server");
        });
        this.socket.on("ahsheep", (msg) => {
            console.log("msg: ", msg);
            //img_array = msg
        });
        /*this.socket.on("predictionWithoutLiquid", (msg) => {
            console.log("msg: ", msg);
            //img_array = msg
        });*/
    }
    disconnect() {
        this.socket.on("disconect", () => {
            console.log("Disconnected from socket server");
        });
    }
    
}

export default new SocketIOService();