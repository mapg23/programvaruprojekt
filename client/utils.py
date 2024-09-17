"""Utils module."""
import subprocess
import sys

def run_cmd(cmd):
    """Function to execute commands on all systems."""
    try:
        res = subprocess.run(cmd, shell=True, check=True, capture_output=True, encoding="UTF-8")
        return res
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
        return None

def get_hwid():
    """Gets os id."""
    if sys.platform.startswith('linux'):
        return run_cmd('cat /etc/machine-id') or \
               run_cmd('cat /var/lib/dbus/machine-id')

    if sys.platform in ['win32', 'cygwin', 'msys']:
        return run_cmd('wmic csproduct get uuid').split('\n')[2].strip()
