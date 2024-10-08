"""Utils module."""
import subprocess
import sys
import platform
import requests

import customtkinter

def run_cmd(cmd):
    """Function to execute commands on all systems."""
    try:
        res = subprocess.run(cmd, shell=True, check=True, capture_output=True, encoding="UTF-8")
        return res.stdout
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
        return None

def create_button(master, text, command=None, padx=10, pady=10):
    """Method to create a ctk button."""
    if command is None:
        button = customtkinter.CTkButton(master=master, text=text)
        button.pack(padx=padx, pady=pady)
    else:
        button = customtkinter.CTkButton(master=master, text=text, command=command)
        button.pack(padx=padx, pady=pady)
    return button

def get_hwid():
    """Gets os id."""
    if sys.platform.startswith('linux'):
        return run_cmd('cat /etc/machine-id') or \
               run_cmd('cat /var/lib/dbus/machine-id')

    if sys.platform in ['win32', 'cygwin', 'msys']:
        return run_cmd('wmic csproduct get uuid').split('\n')[2].strip()

def format_version(version, os_name):
    """Formats the version (linux exclusive)"""
    result = ""
    if os_name in version:
        result = version.replace(os_name, '')
    return result

def get_os_details():
    """Gets os information"""
    return [
        sys.platform,
        format_version(platform.platform(), sys.platform)
    ]

def get_installed_apps_win():
    """Gets installed apps on Windows."""

def get_installed_apps_unix():
    """Gets installed apps on Unix."""
    installed_apps = run_cmd('ls /usr/share/applications')
    apps = installed_apps.split()

    return apps

def get_device_activity():
    """Gets timestamp off when device was in use"""

def get_geolocation():
    """Gets position of device"""
