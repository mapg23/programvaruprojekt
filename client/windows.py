import customtkinter

import api
import utils
import frames

class DeviceWindow(customtkinter.CTkToplevel):
    """Device info class"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("250x400")
        self.title("Device Info")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        self.device_frame = frames.DeviceListFrame(self, data=["OS: Linux", "Version: v10.0"])
        self.device_frame.grid(row=0, column=0, padx=10, pady=(10,0), sticky="nsew")

class AppWindow(customtkinter.CTkToplevel):
    """App info class"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("250x400")
        self.title("App Info")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        if utils.get_os() == "linux":
            apps = utils.get_installed_apps_unix()
        else:
            apps = utils.get_installed_apps_win()

        self.scrollable_checkbox_frame = frames.AppListFrame(self, title="Applications", values=apps)
        self.scrollable_checkbox_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")


class CommandWindow(customtkinter.CTkToplevel):
    """CMD class"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("250x400")
        self.title("Command")

class LogsWindow(customtkinter.CTkToplevel):
    """Logs class"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("250x400")
        self.title("Logs")
