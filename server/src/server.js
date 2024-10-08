"use strict";

module.exports = {
    getAllDevices: get_all_devices
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