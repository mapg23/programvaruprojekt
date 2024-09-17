"""Main module"""
import os

import customtkinter
import api as req
# from client import requests
# import requests


class Main(customtkinter.CTk):
    """Main class"""
    TITLE = "Application"
    GEOMETRY = "800x600"
    INTERVAL = 5000
    SERVER_STATUS = "offline"

    def __init__(self):
        super().__init__()

        self.title(self.TITLE)
        self.geometry(self.GEOMETRY)
        customtkinter.set_appearance_mode("dark")

        self.request = req.Api()

    def heartbeat(self):
        """Heartbeat method"""
        self.SERVER_STATUS = self.request.call_end_point("heartbeat")
        print(os.name)
        self.after(self.INTERVAL, self.heartbeat)

if __name__ == '__main__':
    app = Main()
    app.after(app.INTERVAL, app.heartbeat)
    app.mainloop()
