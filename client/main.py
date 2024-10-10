"""Main module"""
from functools import partial
import json
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

    heartbeat_task = None
    notifcation_task = None

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
        self.api = api.Api()
        self.device = device.Device(utils.get_hwid(), False)


        if self.api.call_without_param("server_status") is not False:
            self.server_status(True)
            self.check_if_in_watch_list()
        else:
            self.server_status(False)

    def check_if_in_watch_list(self):
        """Checks if device already in watchlist"""
        data = json.loads(self.api.call_with_param("check_if_in_watch_list", self.device.get_id()))
        self.device.set_in_watch_list(data['res'])

        if self.device.get_watch_list_status() is True:
            self.update_watchlist_button()
            self.heartbeat_task = self.after(self.interval, self.heartbeat)

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
        self.button_logs = utils.create_button(self, "Logs", command=self.open_logs)

    def open_window(self, window_id):
        """Method to open window"""
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = self.windows[window_id](self)
            self.toplevel_window.get_device(self.device)
            self.toplevel_window.start()
        else:
            self.toplevel_window.focus()

    def open_logs(self):
        """Method for opening logs."""
        if utils.open_logs(self.device.get_os_type()) is False:
            self.open_window(3)
        return

    def upload_file(self):
        """Upload files"""
        files = customtkinter.filedialog.askopenfilename()
        print(files)

    def add_watchlist(self):
        """Watchlist"""
        if self.api.call_without_param("server_status") is False:
            self.timed_notification('Server is offline', 4)
            return

        data = json.loads(self.api.call_with_param("check_if_in_watch_list", self.device.get_id()))
        self.device.set_in_watch_list(data['res'])

        response = None

        if self.device.get_watch_list_status() is False:
            response = json.loads(self.api.call_with_param("add_to_watch_list", self.device.export_device()))
            self.device.set_in_watch_list(True)

            if response['res'] is True:
                self.timed_notification(response["msg"], 4)
                self.update_watchlist_button()
                self.heartbeat_task = self.after(self.interval, self.heartbeat)

    def remove_watchlist(self):
        """Removes device from watchlist"""
        if self.api.call_without_param("server_status") is False:
            self.timed_notification('Server is offline', 4)
            return

        data = json.loads(self.api.call_with_param("remove_from_watchlist", self.device.get_id()))
        self.device.set_in_watch_list(False)

        if data['res'] is True:
            self.timed_notification('Device removed from list', 4)
            self.update_watchlist_button()
            if self.heartbeat_task is not None:
                self.after_cancel(self.heartbeat_task)
                self.heartbeat_task = None

    def update_watchlist_button(self):
        """Updates the watchlist button"""
        if self.device.get_watch_list_status() is True:
            self.button_watchlist.configure(text="Remove from watchlist")
            self.button_watchlist.configure(command=self.remove_watchlist)
        else:
            self.button_watchlist.configure(text="Add to watchlist")
            self.button_watchlist.configure(command=self.add_watchlist)

    def heartbeat(self):
        """Heartbeat method"""
        print("heartbeat")

    def on_dispose(self):
        """Exit method"""
        print("exit")

    def timed_notification(self, text, timer):
        """Shows a notification x seconds."""
        if self.notifcation_task is not None:
            self.after_cancel(self.notifcation_task)

        self.notification_label.configure(text=text)
        self.notifcation_task = self.after(timer * 1000, self.clear_notification)

    def clear_notification(self):
        """Clears notification"""
        self.notification_label.configure(text="")
        self.notifcation_task = None

    def server_status(self, status):
        """Server status text"""
        if status is True:
            self.server_status_label.configure(text="Server: online")
        else:
            self.server_status_label.configure(text="Server: offline")

if __name__ == '__main__':
    app = Main()
    try:
        app.mainloop()
    finally:
        app.on_dispose()
