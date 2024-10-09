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

async function get_all_devices() {
    let sql = `CALL get_all_devices()`;
    let res;

    res = await db.query(sql);

    return res[0];
}

async function remove_device(device_id) {
    let sql =`CALL remove_device(?)`;

    await db.query(sql, device_id);
}

async function get_all_apps(device_id) {
    let sql =`CALL get_apps(?)`;
    let res;

    res = await db.query(sql, device_id);

    return res[0];
}