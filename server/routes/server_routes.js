"use strict";

const express = require("express");
const router = express.Router();

const server = require("../src/server.js");

router.get('/', async (req, res) => {
    let result = await server.getAllDevices();

    let data = {};
    data.res = result;

    res.render("index", data);
});

router.get('/logs:device_id', async (req, res) => {

});

router.get('/cmd:device_id', async (req, res) => {

});

router.get('/apps:device_id', async (req, res) => {

});

router.get('/remove:device_id', async (req, res) => {

});

module.exports = router;