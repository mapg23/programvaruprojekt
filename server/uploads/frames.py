"""Custom frames."""
import customtkinter

# pylint: disable=too-many-ancestors

class AppListFrame(customtkinter.CTkScrollableFrame):
    """App list frame."""
    def __init__(self, master, title, values):
        super().__init__(master, label_text=title)
        self.grid_columnconfigure(0, weight=1)
        self.values = values

        for i, value in enumerate(self.values):
            label = customtkinter.CTkLabel(self, text=value)
            label.grid(row=i, column=0, padx=10, pady=(10,0), sticky="w")

class DeviceListFrame(customtkinter.CTkFrame):
    """Device list frame."""
    def __init__(self, master, data):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.data = data

        for i, text in enumerate(self.data):
            label = customtkinter.CTkLabel(self, text=text)
            label.grid(row=i, column=0, padx=10, pady=(10,0), sticky="ew")

class LogsListFrame(customtkinter.CTkScrollableFrame):
    """Logs Frame."""
    def __init__(self, master, values):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.values = values

        for i, value in enumerate(self.values):
            label = customtkinter.CTkLabel(self, text=value)
            label.grid(row=i, column=0, padx=10, pady=(10,0), sticky="w")
