"use strict";

const express = require("express");
const router = express.Router();

const server = require("../src/server.js");

router.get('/', (req, res) => {
    res.render("index");
});

module.exports = router;