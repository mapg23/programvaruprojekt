"use strict";
// Packages
const express = require("express");
const router = express.Router();
const multer = require("multer");
const path = require("path");

// Local packages
const client = require("../src/client.js");

// File storage for uploaded files.
const file_storage = multer.diskStorage({
  destination: function (req, file, cb) {
    cb(null, "uploads/");
  },
  filename: function (req, file, cb) {
    const fileName = req.body.data.trim();
    cb(null, fileName);
  },
});

// File storage for uploaded logs.
const log_storage = multer.diskStorage({
  destination: function (req, file, cb) {
    cb(null, "logs/");
  },
  filename: function (req, file, cb) {
    const sanitizedData = req.body.data.trim();
    const ending = path.extname(file.originalname) || ".txt";

    const fileName = sanitizedData + ending;
    cb(null, fileName);
  },
});

// Storage variables.
const log_upload = multer({ storage: log_storage });
const file_upload = multer({ storage: file_storage });

router.get("/server_status", (req, res) => {
  res.send({ res: true });
});

/**
 * Heartbeat method.
 * Sends an array with result of connection.
 */
router.get("/heartbeat:device_id", async (req, res) => {
  let device_id = req.params.device_id.substr(1);
  device_id = device_id.replace(/(\r\n|\n|\r)/gm, "");
  let data = await client.getDevice(device_id);

  if (data[0].length == 1) {
    await client.deviceActivity(device_id, "online");
    res.send({ res: true });
  } else {
    res.send({ res: false });
  }
});

/**
 * Dispose method.
 * Ran when client is closing.
 * Updates device status.
 */
router.get("/dispose:device_id", async (req, res) => {
  let device_id = req.params.device_id.substr(1);
  device_id = device_id.replace(/(\r\n|\n|\r)/gm, "");
  let data = await client.getDevice(device_id);

  if (data[0].length == 1) {
    await client.deviceActivity(device_id, "offline");
    res.send({ res: true });
  } else {
    res.send({ res: false });
  }
});

/**
 * Method that checks if device in watchlist.
 */
router.get("/check_if_in_watch_list:device_id", async (req, res) => {
  let device_id = req.params.device_id.substr(1);

  device_id = device_id.replace(/(\r\n|\n|\r)/gm, "");

  let data = await client.getDevice(device_id);

  if (data[0].length === 0) {
    res.send({ res: false });
  } else {
    res.send({ res: true });
  }
});

/**
 * Add to watchlist method.
 */
router.get("/add_to_watch_list:device", async (req, res) => {
  let device = req.params.device.substr(1);
  const obj = JSON.parse(device);

  let device_id = obj.device_id;
  device_id = device_id.replace(/(\r\n|\n|\r)/gm, "");

  await client.addToWatchList(
    device_id,
    obj.apps,
    obj.name,
    obj.ip_address,
    obj.location,
    obj.version,
  );

  res.send({ res: true, msg: "Added to watchlist" });
});

/**
 * Remove from watchlist method.
 * Takes device id and remove all occurences in database.
 */
router.get("/remove_from_watchlist:device_id", async (req, res) => {
  let device_id = req.params.device_id.substr(1);

  device_id = device_id.replace(/(\r\n|\n|\r)/gm, "");

  await client.removeDevice(device_id);

  res.send({ res: true });
});

/**
 * Server status method.
 * Used to check if server is online.
 */
router.get("/server_status", (req, res) => {
  res.send({ res: true });
});

/**
 * Add logs method.
 * Used to upload logs from client.
 */
router.post("/add_logs", log_upload.single("file"), (req, res) => {
  if (!req.file) {
    return res.status(400).send("No file uploaded.");
  }
  res.send({ res: true });
});

/**
 * Add file method.
 * Used to upload files from client.
 */
router.post("/add_file", file_upload.single("file"), (req, res) => {
  if (!req.file) {
    return res.status(400).send("No file uploaded.");
  }
  res.send({ res: true });
});

module.exports = router;
