"use strict";
const express = require('express');
const app = express();
const port = 8083;

app.get('/', (req, res) => {
    res.send("Hello world");
});

app.get('/heartbeat', (req, res) => {
    console.log(req.ip);
    res.send("online");
});

app.listen(port, () => {
    console.log("Listening")
});