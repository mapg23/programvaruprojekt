"""Main module"""
import customtkinter
# from client import requests
# import requests


class Main(customtkinter.CTk):
    """Main class"""
    TITLE = "Application"
    GEOMETRY = "800x600"
    INTERVAL = 5000

    def __init__(self):
        super().__init__()

        self.title(self.TITLE)
        self.geometry(self.GEOMETRY)
        customtkinter.set_appearance_mode("dark")

    def heartbeat(self):
        """Heartbeat method"""
        print("heartbeat")
        self.after(self.INTERVAL, self.heartbeat)

if __name__ == '__main__':
    app = Main()
    app.after(app.INTERVAL, app.heartbeat)
    app.mainloop()
