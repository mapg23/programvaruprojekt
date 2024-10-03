"use strict";
const Device = require('./device');
const express = require('express');
const app = express();
const port = 8083;

//debug group
const watch_list = [];

function get_device(group, id) {
    for (let i = 0; i < group.length; i++) {
        if (group[i].get_id() == id) {
            return i;
        }
    }
    return false;
}

function in_watchlist(group, id) {
    for (const device in group) {
        if (device.get_id() == id) {
            return true;
        }
    }
    return false;
}

app.get('/heartbeat:device_id', (req, res) => {
    res.send("online");
});

app.get('/add_to_watch_list:device_id', (req, res) => {
    if (in_watchlist(watch_list, req.params.device_id)) {
        return;
    }
    let device_id = req.params.device_id;
    device_id = device_id.replace(/(\r\n|\n|\r)/gm, "");
    watch_list.push(new Device(device_id));

});

app.get('/device_info:device_id', (req, res) => {
    if (in_watchlist(watch_list, req.params.device_id)) {
        index = get_device(watch_list, id);
        console.log(index);
    }
});

app.listen(port, () => {
    console.log("Listening")
});