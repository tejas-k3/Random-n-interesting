const http = require("http");
const { send } = require("process");
const WebSocketServer = require("websocket").server;
let connection = null;

const httpServer = http.createServer((req, res) => {
  console.log("Request received!");
});

httpServer.listen(8080, () => console.log("Server is listening on port 8080"))

const websocket = new WebSocketServer({
  httpServer: httpServer,
})

websocket.on("request", request => {
  connection = request.accept(null, request.origin)
  connection.on("open", () => console.log("Connection open!!!"))
  connection.on("close", () => console.log("Connection closed!!!"))
  connection.on("message", message => {
    console.log(`Received message ${message.utf8Data}`)
  })
  sendEvery5Seconds()
})

function sendEvery5Seconds() {
    connection.send(`Message ${Math.random()}`)
    setTimeout(sendEvery5Seconds, 5000)
}

// Run below code on client side in console 
// let wsc = new WebSocket("ws://localhost:8080")
// wsc.onmessage = message => console.log(`We received msg from server ${message.data}`)
// ws.send("Hello server, it's me client")
// ws.close()
