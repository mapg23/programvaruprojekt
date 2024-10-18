#!/usr/bin/env python3
"""Module for unit-testing the device class"""
import unittest
from unittest.mock import patch
import sys
import os

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
