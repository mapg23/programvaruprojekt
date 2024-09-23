"""Main module"""
import customtkinter

# Local import
import api as req
import utils

import ui.dashboard as dashboard

class Main(customtkinter.CTk):
    """Main class"""
    app_title = "Application"
    app_geometry = "800x600"
    interval = 5000
    server_status = "offline"

    def __init__(self):
        super().__init__()

        self.title(self.app_title)
        self.geometry(self.app_geometry)
        customtkinter.set_appearance_mode("dark")

        self.ui()

        self.hwid = utils.get_hwid()
        self.request = req.Api()

        print(utils.get_installed_apps_unix())

    def ui(self):
        """UI method"""
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

        self.dashboard = dashboard.Dashboard(master=self)
        self.dashboard.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

    
    
    def heartbeat(self):
        """Heartbeat method"""
        self.server_status = self.request.call_heart_beat(self.hwid)
        self.dashboard.change_server_status(self.server_status)

        self.after(self.interval, self.heartbeat)

if __name__ == '__main__':
    app = Main()
    app.after(app.interval, app.heartbeat)
    app.mainloop()
