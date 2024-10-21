"use strict";

module.exports = {
    getAllDevices: get_all_devices,
    removeDevice: remove_device,
    getAllApps: get_all_apps
};

const mysql = require('promise-mysql');
const config = require('../config/db.json');
let db;


(async function() {
    db = await mysql.createConnection(config);

    process.on("exit", () => {
        db.end();
    });
})();

/**
 * Method that returns all devices.
 * @returns {Array} - Array of devices.
 */
async function get_all_devices() {
    let sql = `CALL get_all_devices()`;
    let res;

    res = await db.query(sql);

    return res[0];
}

/**
 * Method that removes a device from watchlist.
 * @param {String} device_id - Device id. 
 */
async function remove_device(device_id) {
    let sql =`CALL remove_device(?)`;

    await db.query(sql, device_id);
}

/**
 * Method that returns an array of all applications.
 * Filtered by device_id.
 * @param {String} device_id - Device id.
 * @returns {Array} - Array of applications.
 */
async function get_all_apps(device_id) {
    let sql =`CALL get_apps(?)`;
    let res;

    res = await db.query(sql, device_id);

    return res[0];
}