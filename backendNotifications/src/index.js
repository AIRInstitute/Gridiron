const server = require('./app').server;
/*const io = require('./app').io;

io.on('connection', (socket) => {
  console.log('a user connected');
  socket.on('disconnect', () => {
    console.log('user disconnected');
  });

  socket.on('my message', (msg) => {
    console.log('message: ' + msg);
  });

  socket.on('predictionWithoutLiquid', (msg) => {
    console.log(msg);
  });
  
});
*/
const port = process.env.PORT || 5000;
server.listen(port, () => {
  console.log(`Server listening on: http://localhost:${port}`);
});
