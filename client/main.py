"""Main module"""
from functools import partial
import json
import time

import tkinter
import customtkinter

import device
import utils
import api

from windows import DeviceWindow, AppWindow, LogsWindow


class Main(customtkinter.CTk):
    """Main class"""
    app_title = "Application"
    app_geometry = "800x600"
    in_watchlist = False

    interval = 5000

    windows = {
        1: DeviceWindow,
        2: AppWindow,
        3: LogsWindow
    }

    def __init__(self):
        super().__init__()
        self.title(self.app_title)
        self.geometry(self.app_geometry)
        # self._set_appearance_mode("dark")
        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('dark-blue')

        #ui
        self.create_ui()
        self.toplevel_window = None

        #logic
        self.device = device.Device(utils.get_hwid(), False)
        self.api = api.Api()

    def create_ui(self):
        """Method to create the ui"""
        self.notification_label = customtkinter.CTkLabel(self, text="")
        self.notification_label.pack(padx=10, pady=10)

        self.server_status_label = customtkinter.CTkLabel(self, text="Server status:")
        self.server_status_label.pack(padx=10, pady=10)

        self.button_watchlist = utils.create_button(self, "Add to watchlist", command=self.add_watchlist)

        self.button_device = utils.create_button(self, "Device info", partial(self.open_window, 1))
        self.button_apps = utils.create_button(self, "App list", partial(self.open_window, 2))
        self.button_upload = utils.create_button(self, "Upload file", command=self.upload_file)
        self.button_logs = utils.create_button(self, "Logs", partial(self.open_window, 4))

    def open_window(self, window_id):
        """Method to open window"""
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = self.windows[window_id](self)
            self.toplevel_window.get_device(self.device)
            self.toplevel_window.start()
        else:
            self.toplevel_window.focus()

    def upload_file(self):
        """Upload files"""
        files = customtkinter.filedialog.askopenfilename()
        print(files)

    def add_watchlist(self):
        """Watchlist"""
        data = json.loads(self.api.call_with_param("check_if_in_watch_list", self.device.get_id()))
        self.device.set_in_watch_list(data['res'])

        response = None

        if self.device.get_watch_list_status() is False:
            response = json.loads(self.api.call_with_param("add_to_watch_list", self.device.export_device()))
            self.device.set_in_watch_list(True)

            if response['res'] is True:
                self.timed_notification(response["msg"], 4)
                self.after(self.interval, self.heartbeat)

    def heartbeat(self):
        """Heartbeat method"""
        print("heartbeat")

    def on_dispose(self):
        """Exit method"""
        print("exit")

    def timed_notification(self, text, timer):
        """Shows a notification x seconds."""
        self.notification_label.configure(text=text)
        self.after(timer * 1000, self.clear_notification)

    def clear_notification(self):
        """Clears notification"""
        self.notification_label.configure(text="")

if __name__ == '__main__':
    app = Main()
    try:
        app.mainloop()
    finally:
        app.on_dispose()
