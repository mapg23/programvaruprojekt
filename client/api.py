"""API module"""
import requests

class Api:
    """API class"""
    BASEURL = "http://127.0.0.1"
    PORT = "8083"

    def __init__(self):
        """init"""

    def call_heart_beat(self, device_id, timeout=2000):
        """Call to api for heartbeat"""
        try:
            requests.get(url=f"{self.BASEURL}:{self.PORT}/heartbeat:{device_id}", timeout=timeout)
            return "Online"
        except (requests.ConnectionError):
            return "Offline"

    def call_end_point(self, route, timeout=2000):
        """Call api endpoint"""
        try:
            req = requests.get(url=f"{self.BASEURL}:{self.PORT}/{route}", timeout=timeout)
            return req.status_code
        except (requests.ConnectionError):
            return "Error server offline"

    def call_with_param(self, route, param, timeout=2000):
        """Calls api with parameter."""
        try:
            req = requests.get(url=f"{self.BASEURL}:{self.PORT}/{route}:{param}", timeout=timeout)
            return req.text
        except(requests.ConnectionError):
            return "Error, server offline"
