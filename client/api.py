"""API module"""
import requests

class Api:
    """API class"""
    BASEURL = "http://127.0.0.1"
    PORT = "8083"

    def __init__(self):
        """init"""

    def call_heart_beat(self, timeout=2000):
        """Call to api for heartbeat"""
        try:
            requests.get(url=f"{self.BASEURL}:{self.PORT}/heartbeat", timeout=timeout)
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
