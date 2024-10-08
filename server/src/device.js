"use strict";

class Device {
    constructor(device_id, applications, name, version) {
        this.device_id = device_id;
        this.applications = applications;
        this.name = name;
        this.version = version;
    }

    get_id() {
        return this.device_id;
    }
    
    get_applications() {
        return this.applications;
    }

    set_applications(app_list) {
        this.applications = app_list;
    }
}

module.exports = Device;