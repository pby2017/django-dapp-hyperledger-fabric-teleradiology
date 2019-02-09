//SPDX-License-Identifier: Apache-2.0

var tuna = require('./controller.js');

module.exports = function (app) {
  app.all('/*', function (req, res, next) {
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers", "X-Requested-With");
    next();
  });

  app.get('/get_tuna/:id', function (req, res) {
    tuna.get_tuna(req, res);
  });
  app.get('/add_tuna/:tuna', function (req, res) {
    tuna.add_tuna(req, res);
  });
  app.get('/get_all_tuna', function (req, res) {
    tuna.get_all_tuna(req, res);
  });
  app.get('/change_holder/:holder', function (req, res) {
    tuna.change_holder(req, res);
  });
  app.get('get_opinion/:id', function (req, res) {
    tuna.get_opinion(req, res);
  });
  app.post('/add_opinion', function (req, res) {
    tuna.add_opinion(req,res);
  });
}