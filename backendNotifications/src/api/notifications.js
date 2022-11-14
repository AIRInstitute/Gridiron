const express = require('express');

const router = express.Router();

router.post('/predictionWithLiquid', (req, res) => {
  res.io.emit('predictionWithLiquid', req.body);
  res.send();
});

router.post('/predictionWithoutLiquid', (req, res) => {
  console.log(req.body);
  res.io.emit('predictionWithoutLiquid', req.body);
  res.send();
});

router.post('/resultPipette', (req, res) => {
  res.io.emit('resultPipette', req.body);
  res.send();
});

router.post('/testSuscription', (req, res) => {
  // res.io.emit('resultPipette', req.body);
  // res.send();
  console.log(req.body);
  res.send()
});

module.exports = router;
