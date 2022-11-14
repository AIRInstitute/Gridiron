const express = require('express');
const cors = require('cors');
const morgan = require('morgan');
const helmet = require('helmet');

require('dotenv').config();

const middlewares = require('./middlewares');
const api = require('./api');

const app = express();
const server = require('http').Server(app);
const io = require('socket.io')(server, {
  cors: {
    origin: '*',
    credential: true,
    methods: ["GET", "POST"]
  },
});

app.use(function (req, res, next) {
  res.io = io;
  return next();
});
app.use(cors());
app.use(morgan('dev'));
app.use(helmet());
app.use(express.json({limit: '200mb', extended: true}));
app.use(express.urlencoded({limit: '200mb',extended: true, parameterLimit: 1000000}));

app.get('/', (req, res) => {
  res.json({
    message: 'ah sheep',
  });
  console.log('ah sheep');
  res.io.emit('ahsheep', 'hello sheep');
});

app.use('/api/v1', api);

app.use(middlewares.notFound);
app.use(middlewares.errorHandler);

module.exports = {
  server,
  app,
  io,
};
