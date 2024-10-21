#!/usr/bin/env python3
"""Module for unit-testing the device class"""
import unittest
from unittest.mock import patch, MagicMock
import sys
import os
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from device import Device

class TestDevice(unittest.TestCase):
    """Test class."""

    def test_device_creation(self):
        """Tests device creation"""
        device = Device("hwid1", False)
        self.assertIsInstance(device, Device, "Device object is not an instance of class Device.")

    def test_get_id(self):
        """Tests device id."""
        device = Device("test_id1", False)

        self.assertEqual(device.get_id(), "test_id1", "Device id dosent match.")
        self.assertIs(type(device.get_id()), str, "Id isn't a string.")

    def test_get_logs(self):
        """Tests device.get_logs"""
        device = Device("Hwid", False)
        self.assertIs(type(device.get_logs()), list, "Device.get_logs(), does not return a list.")

    @patch('sys.platform', 'win32')
    def test_get_os_type_windows(self):
        """Tests device get os type."""
        device = Device("Hwid", False)
        device.set_os_type()
        self.assertEqual(device.get_os_type(), 'windows')

    @patch('sys.platform', 'linux')
    def test_get_os_type_linux(self):
        """Tests device get os type."""
        device = Device("Hwid", False)
        device.set_os_type()
        self.assertEqual(device.get_os_type(), 'unix')

    def test_watch_list(self):
        """Tests device set and get in watchlist method."""
        device = Device("Hwid", False)

        self.assertFalse(device.get_watch_list_status())
        device.set_in_watch_list(True)
        self.assertTrue(device.get_watch_list_status())

    @patch('utils.get_installed_apps_unix')
    @patch('utils.get_installed_apps_win')
    def test_set_apps(self,
        mock_get_installed_apps_win,
        mock_get_installed_apps_unix
    ):
        """Tests set app method."""

        #Unix test
        device = Device("Hwid", False)
        device.os_type = "unix"
        mock_get_installed_apps_unix.return_value = ['test1', 'test2']
        device.set_apps()
        self.assertEqual(device.apps, ['test1', 'test2'])

        # Windows test
        device = Device("Hwid", False)
        device.os_type = "windows"
        mock_get_installed_apps_win.return_value = ['win1', 'win2']
        device.set_apps()
        self.assertEqual(device.apps, ['win1', 'win2'])
    
    def test_get_ip_address(self):
        """Tests get ipadress"""
        device = Device("Hwid", False)
        device.ip_address = "127.0.0.1"

        self.assertEqual(device.get_ip_address(), "127.0.0.1")

    def test_get_location(self):
        """Tests get location"""
        device = Device("Hwid", False)
        device.location = "SE"

        self.assertEqual(device.get_location(), "SE")
    
    def test_get_apps(self):
        """Tests get apps."""
        device = Device("HWID", False)
        device.apps = ['test1', 'test2']

        self.assertEqual(device.get_apps(), ['test1', 'test2'])

    def test_get_name(self):
        """Tests get name."""
        device = Device("HWID", False)
        device.os_name = "unix"
        self.assertEqual(device.get_name(), 'unix')

        device.os_name = "windows"
        self.assertEqual(device.get_name(), 'windows')

    def test_get_version(self):
        """Tests get name."""
        device = Device("HWID", False)
        device.os_version = "10"
        self.assertEqual(device.get_version(), '10')

        device.os_version = "1"
        self.assertEqual(device.get_version(), '1')

    def test_export_device(self):
        """Tests export device method."""
        device = Device("hwid", False)
        device.os_name = "os_name"
        device.os_version = "os_version"
        device.ip_address = "ip"
        device.location = "sweden"
        device.apps = ['app1', 'app2']

        data = {
            "device_id": "hwid",
            "name": "os_name",
            "version": "os_version",
            "ip_address": "ip",
            "location": "sweden",
            "apps": ['app1', 'app2']
        }
        self.assertEqual(device.export_device(), json.dumps(data))

    def test_export_logs(self):
        """Tests export logs."""
        device = Device("HWID", False)
        device.logs = "Hello"

        data = {
            "device_id": "HWID",
            "logs": "Hello"
        }

        self.assertEqual(device.export_logs(), json.dumps(data))