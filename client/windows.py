import customtkinter

import api
import utils
import frames

class DeviceWindow(customtkinter.CTkToplevel):
    """Device info class"""
    device = None
    device_frame = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("250x400")
        self.title("Device Info")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def start(self):
        """Start method"""
        data = [
            "OS: " + self.device.get_name(),
            "Version: " + self.device.get_version()
        ]

        self.device_frame = frames.DeviceListFrame(self, data=data)
        self.device_frame.grid(row=0, column=0, padx=10, pady=(10,0), sticky="nsew")

    def get_device(self, device):
        """Getter for device"""
        self.device = device

class AppWindow(customtkinter.CTkToplevel):
    """App info class"""
    device = None
    scrollable_checkbox_frame = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("250x400")
        self.title("App Info")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def start(self):
        """Start method"""
        self.scrollable_checkbox_frame = frames.AppListFrame(self, title="Applications", values=self.device.get_apps())
        self.scrollable_checkbox_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")

    def get_device(self, device):
        """Getter for device"""
        self.device = device

class LogsWindow(customtkinter.CTkToplevel):
    """Logs class"""
    device = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("250x400")
        self.title("Logs")

    def start(self):
        """Start method"""
        print(self.device)

    def get_device(self, device):
        """Getter for device"""
        self.device = device
