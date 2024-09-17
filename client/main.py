"""Main module"""
import customtkinter

# Local import
import api as req
import utils

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

        self.hwid = utils.get_hwid()
        self.request = req.Api()

    def heartbeat(self):
        """Heartbeat method"""
        self.server_status = self.request.call_end_point("heartbeat")
        self.after(self.interval, self.heartbeat)

if __name__ == '__main__':
    app = Main()
    app.after(app.interval, app.heartbeat)
    app.mainloop()
