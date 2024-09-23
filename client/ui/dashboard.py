"""Dashboard module"""
import customtkinter

class Dashboard(customtkinter.CTkFrame):
    """Dashboard class"""
    server_status = ""

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame, for example:
        self.label = customtkinter.CTkLabel(self, text="Server status: no status")
        self.label.grid(row=0, column=0, padx=20)

    def change_server_status(self, status):
        """Changing label for server status"""
        self.label.configure(text=f"Server status: {status}")
