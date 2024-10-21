"use strict";
const express = require("express");
const path = require("path");
const app = express();
const port = 8084;
const serveIndex = require("serve-index");

const client_route = require("./routes/client_routes.js");
const server_route = require("./routes/server_routes.js");

app.set("view engine", "ejs");
app.use(express.static(path.join(__dirname, "public")));

//routes
app.use("/client", client_route);
app.use("/server", server_route);

app.get("/", (req, res) => {
  res.redirect("/server");
});

app.use("/uploads", serveIndex(path.join(__dirname, "uploads")));
app.use("/uploads", express.static(path.join(__dirname, "uploads")));

app.listen(port, () => {
  console.log(`Server started on port: ${port}`);
});
