"use strict";
// Packages
const express = require("express");
const router = express.Router();
const fs = require('fs').promises;
const { dirname } = require('path');
const path = require('path');

// Local packages
const server = require("../src/server.js");

const rootDir = dirname(require.main.filename);

/**
 * Method that reads from file.
 * @param {String} filePath - File path.
 * @returns {Promise<String>} - Returns a promise of a string.
 */
async function getLogs(filePath) {
    try {
        const data = await fs.readFile(filePath, 'utf8');
        return data;
    } catch {
        return false;
    }
}

/**
 * Gets all devices and render index page.
 */
router.get('/', async (req, res) => {
    let result = await server.getAllDevices();

    let data = {};
    data.res = result;

    res.render("index", data);
});

/**
 * Get logs from device id and renders logs page.
 */
router.get('/logs/:device_id', async (req, res) => {

    const device_id = req.params.device_id;
    const filePath = path.join(rootDir, "logs", `${device_id}.txt`);

    let log_res = await getLogs(filePath);

    if (log_res == false) {
        res.status(500).json({ error: "Failed to read log file."});
    }

    const logs = log_res.split('\n');

    let data = {};
    data.res = logs;

    res.render("logs", data);
});

/**
 * Gets all apps from device id and renders app page.
 */
router.get('/apps/:device_id', async (req, res) => {
    let device_id = req.params.device_id;
    let result = await server.getAllApps(device_id);
    let data = {};
    data.res = result;

    res.render("app_list", data);
});

/**
 * Route used to remove a device from watchlist using device id.
 */
router.get('/remove/:device_id', async (req, res) => {
    let device_id = req.params.device_id;
    await server.removeDevice(device_id);
    res.redirect("/");
});

module.exports = router;