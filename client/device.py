"""Device module"""
import sys
import json
import utils

class Device:
    """Device class"""
    os_type = ""
    apps = []
    ip_address = ""
    os_name = ""
    os_version = ""
    location = ""
    logs = []

    def __init__(self, hwid, in_watch_list = False,):
        self.hwid = hwid
        self.in_watch_list = in_watch_list

        self.set_os_type()
        self.set_apps()

        self.os_name = utils.get_os_name()
        self.os_version = utils.get_os_version()

        self.ip_address, self.location = utils.get_ip_and_location()
        self.logs = utils.export_logs()

    def get_logs(self):
        """Getter for logs"""
        return self.logs

    def set_in_watch_list(self, response):
        """Setter for watchlist"""
        self.in_watch_list = response

    def get_watch_list_status(self):
        """Getter for watchlist"""
        return self.in_watch_list

    def get_os_type(self):
        """Getter for os_type."""
        return self.os_type

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
    def get_ip_address(self):
        """Getter for ip"""
        return self.ip_address
    
    def get_location(self):
        """Getter for location"""
        return self.location

    def get_id(self):
        """Getter for id."""
        return self.hwid

    def get_apps(self):
        """Getter for apps"""
        return self.apps

    def get_name(self):
        """Getter for name"""
        return self.os_name

    def get_version(self):
        """Getter for version"""
        return self.os_version

    def export_device(self):
        """Exports class to json"""
        data = {
            "device_id": self.get_id(),
            "name": self.get_name(),
            "version": self.get_version(),
            "ip_address": self.ip_address,
            "location": self.location,
            "apps": self.get_apps(),
        }

        return json.dumps(data)
