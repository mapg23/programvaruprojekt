"""Main module"""
from functools import partial
import atexit

import tkinter
import customtkinter
import utils
import api

from windows import DeviceWindow, AppWindow, CommandWindow, LogsWindow


class Main(customtkinter.CTk):
    """Main class"""
    app_title = "Application"
    app_geometry = "800x600"
    in_watchlist = False

    interval = 5000

    windows = {
        1: DeviceWindow,
        2: AppWindow,
        3: CommandWindow,
        4: LogsWindow
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

        self.server_status = ""
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
        self.button_cmd = utils.create_button(self, "Cmd", partial(self.open_window, 3))
        self.button_logs = utils.create_button(self, "Logs", partial(self.open_window, 4))

    def open_window(self, window_id):
        """Method to open window"""
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = self.windows[window_id](self)
        else:
            self.toplevel_window.focus()

    def add_watchlist(self):
        """Watchlist"""
        self.api.call_with_param("add_to_watch_list", utils.get_hwid())

    def heartbeat(self):
        """Heartbeat method"""
        self.server_status = self.api.call_heart_beat(utils.get_hwid())
        self.server_status_label.configure(text=f"Server status: {self.server_status}")
        # self.after(self.interval, f"Server status: {self.server_status}")

    def on_dispose(self):
        """Exit method"""
        print("exit")

if __name__ == '__main__':
    app = Main()
    try:
        app.after(app.interval, app.heartbeat)
        app.mainloop()
    finally:
        app.on_dispose()
