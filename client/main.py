"""Main module"""
from functools import partial

import tkinter
import customtkinter
import utils

from windows import DeviceWindow, AppWindow, CommandWindow, LogsWindow


class Main(customtkinter.CTk):
    """Main class"""
    app_title = "Application"
    app_geometry = "800x600"

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

    def create_ui(self):
        """Method to create the ui"""
        self.notification_label = customtkinter.CTkLabel(self, text="")
        self.notification_label.pack(padx=10, pady=10)

        self.server_status_label = customtkinter.CTkLabel(self, text="Server status:")
        self.server_status_label.pack(padx=10, pady=10)

        self.button_watchlist = utils.create_button(self, "Add to watchlist")

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

    def heartbeat(self):
        """Heartbeat method"""
        self.after(self.interval, self.heartbeat)

if __name__ == '__main__':
    app = Main()
    app.after(app.interval, app.heartbeat)
    app.mainloop()
