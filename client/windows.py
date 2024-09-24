import customtkinter

class DeviceWindow(customtkinter.CTkToplevel):
    """Device info class"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("250x400")
        self.title("Device Info")

class AppWindow(customtkinter.CTkToplevel):
    """App info class"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("250x400")
        self.title("App Info")

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
