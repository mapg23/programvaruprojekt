"use strict";

class Device {
    constructor(device_id) {
        this.device_id = device_id;
    }

    get_id() {
        return this.device_id;
    }

    get_applications() {

    }
}


module.exports = Device;