"use strict";

module.exports = {
    addToWatchList: add_to_watch_list,
    getDevice: get_device
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

async function add_to_watch_list(id, apps, name, version) {
    let sql = `CALL add_device(?,?,?,?,?,?);`;
    let res;
    
    res = await db.query(sql, [id, name, version, 'location', 'last_active', 'device_status']);
    
    add_apps(id, apps);

    return res;
}

async function add_apps(id, apps) {
    for (const app of apps) {
        let sql = `CALL add_app(?,?,?)`;
        
        await db.query(sql, [id, app, '']);
    }
}

async function get_device(id) {
    let sql = `CALL get_device(?)`;
    let res;

    res = await db.query(sql, id);

    return res;
}