"use strict";
const express = require('express');
const app = express();
const port = 8083;

app.get('/', (req, res) => {
    res.send("Hello world");
});

app.get('/heartbeat', (req, res) => {
    res.send("confirmed");
});

app.listen(port, () => {
    console.log("Listening")
});