"use strict";
const Device = require('./device');

const express = require('express');
const app = express();
const port = 8083;

//debug group
const debug_group = [];

/**
 * Debug function
 * @param {*} group 
 * @param {*} new_id 
 * @returns boolean
 */
function filterDevices(group, new_id) {
    for (const device of group) {
        if (device.get_id() == new_id) {
            return true;
        }
    }
    return false;
}

app.get('/', (req, res) => {
    res.send("Hello world");
});

app.get('/heartbeat:device_id', (req, res) => {

    if (!filterDevices(debug_group, req.params.device_id)) {
        debug_group.push(new Device(req.params.device_id));
    }
    res.send("online");

    console.log(debug_group);
});

app.get('/get_applications:app_list', (req, res) => {
    res.send("list");
});

app.listen(port, () => {
    console.log("Listening")
});