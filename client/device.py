"""Device module"""
import sys
import json

import utils

class Device:
    """Device class"""
    os_type = ""
    apps = []

    def __init__(self, hwid, details = ['os_name', 'os_version'], in_watch_list = False,):
        self.hwid = hwid
        self.details = details
        self.in_watch_list = in_watch_list

        self.set_os_type()
        self.set_apps()

    def set_in_watch_list(self, response):
        """Setter for watchlist"""
        self.in_watch_list = response

    def get_watch_list_status(self):
        """Getter for watchlist"""
        return self.in_watch_list

    def set_os_type(self):
        """Determines os type"""
        if sys.platform.startswith('linux'):
            self.os_type = "unix"
        if sys.platform in ['win32', 'cygwin', 'msys']:
            self.os_type = "windows"

    def set_apps(self):
        """Method to set applications"""
        if self.os_type == "unix":
            self.apps = utils.get_installed_apps_unix()
        elif self.os_type == "windows":
            self.apps = utils.get_installed_apps_win()

    def get_id(self):
        """Getter for id."""
        return self.hwid

    def get_apps(self):
        """Getter for apps"""
        return self.apps

    def get_name(self):
        """Getter for name"""
        return self.details[0]

    def get_version(self):
        """Getter for version"""
        return self.details[1]

    def export_device(self):
        """Exports class to json"""
        data = {
            "device_id": self.get_id(),
            "apps": self.get_apps(),
            "name": self.get_name(),
            "version": self.get_version()
        }

        return json.dumps(data)
