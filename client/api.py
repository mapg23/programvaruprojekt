"""API module"""
import requests

class Api:
    """API class"""
    BASEURL = "http://127.0.0.1"
    PORT = "8083"

    def __init__(self):
        """init"""

    def call_end_point(self, route, timeout=2000):
        """Call api endpoint"""
        try:
            req = requests.get(url=f"{self.BASEURL}:{self.PORT}/{route}", timeout=timeout)
            return req.status_code
        except (requests.ConnectionError):
            return "Offline"
