"""Main module"""
from functools import partial
import json
import os
import threading

import customtkinter
from pystray import MenuItem, Icon

from PIL import Image

import device
import utils
import api

from windows import DeviceWindow, AppWindow, LogsWindow

class Main(customtkinter.CTk):
    #General variables
    app_title = "Application"
    app_geometry = "800x600"

    # Logic variables
    in_watchlist = False
    interval = 5000

    # Thread variables
    heartbeat_task = None
    notifcation_task = None

    # Ui variables
    windows = {
        1: DeviceWindow,
        2: AppWindow,
        3: LogsWindow
    }

    # Systray variables
    icon_path = "icon.jpg"

    def __init__(self):
        super().__init__()

        # Geometry
        self.title(self.app_title)
        self.geometry(self.app_geometry)

        # Themes
        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('dark-blue')

        utils.append_logs("[C2]: initialized")
        # ui section
        self.create_ui()
        self.toplevel_window = None

        # logic section
        self.api = api.Api()
        self.device = device.Device(utils.get_hwid(), False)


        if self.api.call_without_param("server_status") is not False:
            utils.append_logs("[C2]: Checking server status: true")
            self.server_status(True)
            self.check_if_in_watch_list()
        else:
            utils.append_logs("[C2]: Checking server status: false")
            self.server_status(False)

        # systray section
        self.menu = (
            MenuItem('Add to watchlist', self.systray_start),
            MenuItem('Remove from watchlist', self.systray_stop),
            MenuItem('Maximize window', self.show_window),
            MenuItem('Exit', self.exit_action)
        )
        # systray icon
        self.icon = Icon("C2_icon", Image.open(self.icon_path), "C2", self.menu)
        # start a thread for icon
        threading.Thread(target=self.run_icon, daemon=True).start()

        self.protocol("WM_DELETE_WINDOW", self.hide_window)  # Hide on close
        self.mainloop()

# Ui Methods

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

    def update_watchlist_button(self):
        """Updates the watchlist button"""
        if self.device.get_watch_list_status() is True:
            self.button_watchlist.configure(text="Remove from watchlist")
            self.button_watchlist.configure(command=self.remove_watchlist)
        else:
            self.button_watchlist.configure(text="Add to watchlist")
            self.button_watchlist.configure(command=self.add_watchlist)

    def open_window(self, window_id):
        """Method to open window"""
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = self.windows[window_id](self)
            self.toplevel_window.get_device(self.device)
            self.toplevel_window.start()
        else:
            self.toplevel_window.focus()

# Logic Methods

    def upload_file(self):
        """Upload files"""
        file_path = customtkinter.filedialog.askopenfilename()
        file_name = os.path.basename(file_path)
        self.api.post_file("add_file", file_path, file_name)
        utils.append_logs(f"[C2]: file: {file_name}, has been uploaded to server")
        self.timed_notification('File uploaded', 4)

    def open_logs(self):
        """Method for opening logs."""
        utils.append_logs("[C2]: logs opened")
        if utils.open_logs(self.device.get_os_type()) is False:
            self.open_window(3)
        return

    def heartbeat(self):
        """Heartbeat method"""
        response = json.loads(self.api.call_with_param("heartbeat", self.device.get_id()))

    def add_watchlist(self):
        """Watchlist"""
        if self.api.call_without_param("server_status") is False:
            utils.append_logs("[C2]: Tried to add to watchlist error server offline")
            self.timed_notification('Server is offline', 4)
            return

        data = json.loads(self.api.call_with_param("check_if_in_watch_list", self.device.get_id()))
        self.device.set_in_watch_list(data['res'])

        response = None

        if self.device.get_watch_list_status() is False:
            response = json.loads(self.api.call_with_param("add_to_watch_list", self.device.export_device()))
            self.device.set_in_watch_list(True)

            if response['res'] is True:
                log_res = self.api.post_file("add_logs", "logs.txt", self.device.get_id())
                self.timed_notification(response["msg"], 4)
                utils.append_logs(f"[C2]: {self.device.get_id()} has been added to watchlist")
                self.update_watchlist_button()
                self.heartbeat_task = self.after(self.interval, self.heartbeat)

    def remove_watchlist(self):
        """Removes device from watchlist"""
        if self.api.call_without_param("server_status") is False:
            utils.append_logs("[C2]: Tried to remove from watchlist, erorr server offline")
            self.timed_notification('Server is offline', 4)
            return

        data = json.loads(self.api.call_with_param("remove_from_watchlist", self.device.get_id()))
        self.device.set_in_watch_list(False)

        if data['res'] is True:
            self.timed_notification('Device removed from list', 4)
            utils.append_logs(f"[C2]: {self.device.get_id()}, have been remove from watchlist")
            self.update_watchlist_button()

            if self.heartbeat_task is not None:
                self.after_cancel(self.heartbeat_task)
                self.heartbeat_task = None
                utils.append_logs("[C2]: Heartbeat has been removed")

    def check_if_in_watch_list(self):
        """Checks if device already in watchlist"""
        data = json.loads(self.api.call_with_param("check_if_in_watch_list", self.device.get_id()))
        self.device.set_in_watch_list(data['res'])

        if self.device.get_watch_list_status() is True:
            utils.append_logs(f"[C2]: in watchlist as {self.device.get_id()}")
            utils.append_logs(f"[C2]: starting heartbeat for {self.device.get_id()}")
            self.update_watchlist_button()
            self.heartbeat_task = self.after(self.interval, self.heartbeat)

# systray methods

    def systray_start(self):
        """Callback for systray"""
        if self.device.get_watch_list_status() is True:
            return
        self.add_watchlist()

    def systray_stop(self):
        """Callback for systray"""
        if self.device.get_watch_list_status() is False:
            return
        self.remove_watchlist()

    def run_icon(self):
        """Run the system tray icon."""
        self.icon.run()

    def exit_action(self, icon, item):
        """Exit the application from the system tray."""
        self.api.call_with_param("dispose", self.device.get_id())
        self.quit()  # Close the gui
        icon.stop()  # Stop the systray

    def hide_window(self):
        """Hide the window instead of closing it."""
        self.withdraw()

    def show_window(self):
        """Shows window"""
        self.deiconify()

    def run(self):
        """Run the system tray and gui window."""
        self.icon.run()

if __name__ == "__main__":
    app = Main()
