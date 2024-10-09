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

router.get('/apps/:device_id', async (req, res) => {
    let device_id = req.params.device_id;
    let result = await server.getAllApps(device_id);
    let data = {};
    data.res = result;

    res.render("app_list", data);
});

router.get('/remove/:device_id', async (req, res) => {
    let device_id = req.params.device_id;
    await server.removeDevice(device_id);
    res.redirect("/");
});

module.exports = router;