import customtkinter
import api
import utils

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

        self.app_list = utils.get_installed_apps_unix()

        print(self.app_list)

        # self.scroll_frame = customtkinter.CTkScrollableFrame(self, width=230, height=400)
        # self.scroll_frame.grid(row=0, column=0, padx=0, pady=0)

        # counter = 0
        # for app in self.app_list:
        #     label = customtkinter.CTkLabel(self.scroll_frame, text=app)
        #     label.grid(row=counter, column=0, pady=10)
        #     counter += 1




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
