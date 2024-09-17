"""Main module"""
import os, sys, subprocess

import customtkinter
import api as req
# from client import requests
# import requests

class Main(customtkinter.CTk):
    """Main class"""
    TITLE = "Application"
    GEOMETRY = "800x600"
    INTERVAL = 5000
    SERVER_STATUS = "offline"

    def __init__(self):
        super().__init__()

        self.title(self.TITLE)
        self.geometry(self.GEOMETRY)
        customtkinter.set_appearance_mode("dark")

        self.get_hwid()
        self.request = req.Api()

    def run_cmd(self, cmd):
        """Runs a command"""
        try:
            res = subprocess.run(cmd, shell=True, check=True, capture_output=True, encoding="UTF-8")
            return res.stdout().strip()
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
            return None

    def get_hwid(self):
        """Get id method"""
        if sys.platform.startswith('linux'):
            return self.run_cmd('cat /etc/machine-id') or \
                   self.run_cmd('cat /var/lib/dbus/machine-id')

        if sys.platform in ['win32', 'cygwin', 'msys']:
            return self.run_cmd('wmic csproduct get uuid').split('\n')[2].strip()

    def heartbeat(self):
        """Heartbeat method"""
        self.SERVER_STATUS = self.request.call_end_point("heartbeat")
        print(os.name)
        self.after(self.INTERVAL, self.heartbeat)

if __name__ == '__main__':
    app = Main()
    app.after(app.INTERVAL, app.heartbeat)
    app.mainloop()
