"use strict";

const express = require("express");
const router = express.Router();

const client = require("../src/client.js");

router.get('/', (req, res) => {
    res.send("Hello from client")
});

router.get('/server_status', (req, res) =>  {
    res.send({res: true});
});

router.get('/heartbeat:device_id', (req, res) => {
    console.log("heartbeat");
});

router.get('/check_if_in_watch_list:device_id', async (req, res) => {
    let device_id = req.params.device_id.substr(1);

    device_id = device_id.replace(/(\r\n|\n|\r)/gm, "");

    let data = await client.getDevice(device_id);

    if(data[0].length === 0) {
        res.send({res: false});
    } else {
        res.send({res: true});
    }
});

router.get('/add_to_watch_list:device', async (req, res) => {
    let device = req.params.device.substr(1);
    const obj = JSON.parse(device);


    let device_id = obj.device_id;
    device_id = device_id.replace(/(\r\n|\n|\r)/gm, "");
    console.log(obj.ip_address);
    await client.addToWatchList(device_id, obj.apps, obj.name, obj.ip_address, obj.location, obj.version);

    res.send({res: true, msg: 'Added to watchlist'});
});

router.get('/remove_from_watchlist:device_id', async (req, res) => {
    let device_id = req.params.device_id.substr(1);

    device_id = device_id.replace(/(\r\n|\n|\r)/gm, "");

    await client.removeDevice(device_id);

    res.send({res: true})
});

router.get('/server_status', (req, res) => {
    res.send({res: true})
});

 
module.exports = router;