"use strict";

module.exports = {
    addToWatchList: add_to_watch_list,
    getDevice: get_device,
    removeDevice: remove_device,
    deviceActivity: device_activity
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
 * Adds a device to the watchlist.
 * @param {String} id - Device id.
 * @param {Array} apps - App array.
 * @param {String} name - Device name.
 * @param {String} ip_address - Ipaddress.
 * @param {String} location - Geolocation.
 * @param {String} version - Version of device.
 * @returns {Any} - Returns result of query.
 */
async function add_to_watch_list(id, apps, name, ip_address, location, version) {
    let sql = `CALL add_device(?,?,?,?,?,?,?);`;
    let res;
    
    res = await db.query(sql, [id, name, version, location, ip_address, 'last_active', 'device_status']);
    
    add_apps(id, apps);

    return res;
}

/**
 * Method to add apps.
 * @param {String} id - Device id.
 * @param {Array} apps - App array.
 * @returns void
*/
async function add_apps(id, apps) {
    for (const app of apps) {
        let sql = `CALL add_app(?,?,?)`;
        
        await db.query(sql, [id, app, '']);
    }
}

/**
 * Method to return row that matches the device id.
 * @param {String} id - Device id.
 * @returns {Array} - row that matches.
 */
async function get_device(id) {
    let sql = `CALL get_device(?)`;
    let res;

    res = await db.query(sql, id);

    return res;
}

/**
 * Method that removes the device from the watchlist.
 * @param {String} id - Device id. 
 * @returns {Array} - Returns confirmation.
 */
async function remove_device(id) {
    let sql = `CALL remove_device(?)`;
    let res;

    res = await db.query(sql, id);

    return res;
}

/**
 * Method that updates device activity.
 * @param {String} id - Device id. 
 * @param {String} device_status - Offline/Online.
 * @returns {Array} - Confirmation
 */
async function device_activity(id, device_status) {
    let sql = `CALL update_status(?,?)`;
    let res;

    res = await db.query(sql, [id, device_status]);

    return res;
}