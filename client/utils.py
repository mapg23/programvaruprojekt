"""Utils module."""
import subprocess
import sys
import platform 

# windows only import
try:
    from windows_tools.installed_software import get_installed_software
except (ModuleNotFoundError):
    pass

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

def get_ip_and_location():
    """Get ip and location"""
    # Send request to ipinfo.io to get details based on your public IP address
    response = requests.get('https://ipinfo.io/', timeout=2000)

    if response.status_code == 200:
        data = response.json()

        country = data.get('country')  # Extract the country from the response
        ip = data.get('ip')
        return [ip, country]

    return ["Unknown", "Unknown"]


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

def get_os_name():
    """Gets os name"""
    name = platform.platform().split('-')[0]
    return name

def get_os_version():
    """Gets os version"""
    return platform.release()

def get_installed_apps_win():
    """Gets installed apps on Windows."""
    apps = []

    for software in get_installed_software():
        if software['name'] == '':
            continue

        apps.append(software['name'])

    return apps

def get_installed_apps_unix():
    """Gets installed apps on Unix."""
    installed_apps = run_cmd('ls /usr/share/applications')
    apps = installed_apps.split()

    return apps

def get_device_activity():
    """Gets timestamp off when device was in use"""

def get_geolocation():
    """Gets position of device"""
