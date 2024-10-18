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

    try:
        from windows_tools.installed_software import get_installed_software
        for software in get_installed_software():
            if software['name'] == '':
                continue
            apps.append(software['name'])
        return apps
    except ModuleNotFoundError:
        return apps

def get_installed_apps_unix():
    """Gets installed apps on Unix."""
    installed_apps = run_cmd('ls /usr/share/applications')

    # dummy data
    if installed_apps is None:
        installed_apps = "test1\ntest2"

    apps = installed_apps.split()

    return apps

def open_logs(os_type):
    """Method to open logs with default file viewer."""
    if os_type == 'unix':
        run_cmd('open logs.txt')
        return True
    if os_type == 'windows':
        run_cmd('start logs.txt')
        return True
    return False

def append_logs(text):
    """Appends logs."""
    with open("logs.txt", 'a') as writer:
        writer.write(text + "\n")
    writer.close()

def export_logs():
    """Exports logs"""
    logs = []
    with open("logs.txt", mode="r", encoding="utf-8") as reader:
        logs.append(reader.readlines())
    reader.close()

    return logs
