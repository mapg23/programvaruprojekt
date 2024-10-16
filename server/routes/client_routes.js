"use strict";

const express = require("express");
const router = express.Router();

const multer = require('multer');
const path = require('path');

const client = require("../src/client.js");

const file_storage = multer.diskStorage({
    destination: function (req, file, cb) {
        cb(null, 'uploads/');
    },
    filename: function (req, file, cb) {
        const fileName = req.body.data.trim();
        cb(null, fileName);
    }
});

const log_storage = multer.diskStorage({
    destination: function (req, file, cb) {
        cb(null, 'logs/');
    },
    filename: function (req, file, cb) {
        const sanitizedData = req.body.data.trim();
        const ending = path.extname(file.originalname) || '.txt';

        const fileName = sanitizedData + ending;
        cb(null, fileName);
    }
});

// Multer variables
const log_upload = multer({storage: log_storage});
const file_upload = multer({storage: file_storage});

router.get('/server_status', (req, res) =>  {
    res.send({res: true});
});

router.get('/heartbeat:device_id', async (req, res) => {
    let device_id = req.params.device_id.substr(1);
    device_id = device_id.replace(/(\r\n|\n|\r)/gm, "");
    let data = await client.getDevice(device_id);

    if(data[0].length == 1) {
        await client.deviceActivity(device_id, 'online');
        res.send({res: true})
    } else {
        res.send({res: false})
    }
});

router.get('/dispose:device_id', async (req, res) => {
    let device_id = req.params.device_id.substr(1);
    device_id = device_id.replace(/(\r\n|\n|\r)/gm, "");
    let data = await client.getDevice(device_id);
    
    if(data[0].length == 1) {
        await client.deviceActivity(device_id, 'offline');
        res.send({res: true})
    } else {
        res.send({res: false})
    }
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

router.post('/add_logs', log_upload.single('file'), (req, res) => {
    if (!req.file) {
        return res.status(400).send('No file uploaded.');
    }
    res.send({res: true})
});

router.post('/add_file', file_upload.single('file'), (req, res) => {
    if (!req.file) {
        return res.status(400).send('No file uploaded.');
    }
    res.send({res: true})
});

 
module.exports = router;