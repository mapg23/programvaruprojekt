#!/usr/bin/env python3
"""Module for unit-testing the utils"""
import unittest
from unittest.mock import patch, MagicMock
import sys
import os
import subprocess

import customtkinter


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

import utils

class TestUtils(unittest.TestCase):
    """Test class."""

    @patch('utils.subprocess.run')
    def test_run_cmd_sucess(self, mock_run):
        """Tests run_cmd on success"""
        mock_run.return_value = MagicMock(stdout="output")

        result = utils.run_cmd("echo 'example'")

        self.assertEqual(result, "output")

    @patch('utils.subprocess.run')
    def test_run_cmd_timeout(self, mock_run):
        """Tests run_cmd on timeout"""
        mock_run.side_effect = subprocess.TimeoutExpired(cmd='cmd', timeout=3)
        result = utils.run_cmd("command")
        self.assertIsNone(result)

    @patch('utils.subprocess.run')
    def test_run_cmd_error(self, mock_run):
        """Tests run_cmd on error"""
        mock_run.side_effect = subprocess.CalledProcessError(1, 'cmd')
        result = utils.run_cmd('command')
        self.assertIsNone(result)

    @patch('utils.requests.get')
    def test_get_ip_and_location(self, mock):
        """Tests create button."""
        mock_response = MagicMock()
        mock_response.status_code = 404

        mock.return_value = mock_response

        result = utils.get_ip_and_location()

        self.assertEqual(result, ['Unknown', 'Unknown'])

    @patch('sys.platform', 'linux')
    @patch('utils.run_cmd')
    def test_get_hwid_linux(self, command_mock):
        """Tests get hwid linux."""
        command_mock.side_effect = ['hwid']
        result = utils.get_hwid()
        self.assertEqual(result, 'hwid')

    @patch('sys.platform', 'win32')
    @patch('utils.run_cmd')
    def test_get_hwid_windows(self, command_mock):
        """Tests get hwid windows"""
        command_mock.return_value = "Product\nUUID\nHWID\n"
        result = utils.get_hwid()
        self.assertEqual(result, 'HWID')

    @patch('sys.platform', 'unknown')
    def test_get_hwid_unknown(self):
        """Tests get hwid on unknown os."""
        result = utils.get_hwid()
        self.assertEqual(result, "Dummy hwid")

    @patch('utils.run_cmd')
    def test_get_installed_apps_unix(self, command_mock):
        """Tests get installed apps unix."""
        command_mock.return_value = None
        result = utils.get_installed_apps_unix()
        self.assertEqual(result, ['test1', 'test2'])

    @patch('utils.run_cmd')
    def test_open_logs_unix(self, cmd_mock):
        """Tests open_logs"""
        result = utils.open_logs("unix")
        self.assertTrue(result)

    @patch('utils.run_cmd')
    def test_open_logs_win(self, cmd_mock):
        """Tests open_logs"""
        result = utils.open_logs("windows")
        self.assertTrue(result)

    @patch('utils.run_cmd')
    def test_open_logs_none(self, cmd_mock):
        """Tests open logs."""
        result = utils.open_logs("darwin")
        self.assertFalse(result)