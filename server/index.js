"use strict";
const express = require('express');
const path = require('path');
const app = express();
const port = 8083;

const minutes = 5, interval = minutes * 60 * 1000;

const client_route = require('./routes/client_routes.js');
const server_route = require('./routes/server_routes.js');

app.set("view engine", "ejs");
app.use(express.static(path.join(__dirname, "public")));

//routes
app.use("/client", client_route);
app.use("/server", server_route);

setInterval(function() {
    console.log("check");
}, interval);

app.get('/', (req, res) => {
    res.redirect('/server');
})

app.listen(port, () => {
    console.log("Listening")
});