// imports
const express = require("express");
const cors = require("cors")

// Setup Server
var server = express();
var port = 4200;

var bodyParser = require('body-parser')

// parse application/x-www-form-urlencoded
server.use(bodyParser.urlencoded({ extended: false }))

// parse serverlication/json
server.use(bodyParser.json())

// Middleware
server.use(function (req, res, next) {
    res.header("Access-Control-Allow-Origin", req.get("origin"));
    res.header("Access-Control-Allow-Credentials", "true");
    next();
});
server.options("*", function (req, res, next) {
    res.header("Access-Control-Allow-Headers", "Content-type");
    next();
});

server.use(cors())


server.listen(port, function () {
    console.log("Listening on " + port);
})

server.get("/find", function (req, res) {
    console.log("get")
    res.send({ name: "ooga booga" })
})

server.post("/find", function (req, res) {
    console.log(req.body)
    var spawn = require("child_process").spawn;

    var process = spawn('python', ["./../song_grid.py",
        {
            loudness: req.body.loudness,
            tempo: req.body.tempo,
            duration: req.body.duration,
            bullshit: 0
        }]);

    process.stdout.on('data', function (data) {
        res.send(data.toString());
    })
    res.send({ data: req.body })
})