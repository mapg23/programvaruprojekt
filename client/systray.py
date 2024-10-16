import tkinter as tk
from tkinter import messagebox
import webbrowser
from PIL import Image, ImageDraw
import pystray
from pystray import MenuItem, Icon

class MinimizedApp:
    """System tray class."""
    def __init__(self):
        # Create a menu for the system tray
        self.menu = (
            MenuItem('Start', self.show_message),
            MenuItem('Stop', self.open_url),
            MenuItem('Exit', self.exit_action)
        )

        # Create the icon
        self.icon = Icon("test_icon", self.create_image(64, 64), "Tray App", self.menu)

    def create_image(self, width, height):
        """Create an image for the system tray icon."""
        # Generate an image and draw a pattern
        image = Image.new('RGB', (width, height), color=(255, 255, 255))
        dc = ImageDraw.Draw(image)
        dc.rectangle(
            (width // 4, height // 4, width * 3 // 4, height * 3 // 4),
            fill=(0, 100, 255),
            outline=(0, 0, 0)
        )
        return image

    def show_message(self):
        """Display a message box."""
        messagebox.showinfo("Message", "Hello! This is a system tray application.")

    def open_url(self):
        """Open a specified URL in the default web browser."""
        webbrowser.open("https://www.example.com")

    def exit_action(self, icon, item):
        """Exit the application."""
        icon.stop()

    def run(self):
        """Run the system tray icon."""
        self.icon.run()


if __name__ == "__main__":
    app = MinimizedApp()
    app.run()
