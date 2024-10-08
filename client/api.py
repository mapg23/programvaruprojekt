"""API module"""
import requests

class Api:
    """API class"""
    BASEURL = "http://127.0.0.1:8083/client"

    def __init__(self):
        """init"""

    def call_without_param(self, route, timeout=2000):
        """Call api endpoint"""
        try:
            req = requests.get(url=f"{self.BASEURL}/{route}", timeout=timeout)
            return req.status_code
        except (requests.ConnectionError):
            return "Error server offline"

    def call_with_param(self, route, param, timeout=2000):
        """Calls api with parameter."""
        try:
            req = requests.get(url=f"{self.BASEURL}/{route}:{param}", timeout=timeout)
            return req.text
        except(requests.ConnectionError):
            return "Error, server offline"
