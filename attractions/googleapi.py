import requests

from moreaboutattractions.settings import GOOGLE_API_KEY


class GoogleApi():
    location = ""
    result = ""

    def __init__(self):
        self.send_request()

    def __str__(self):
        return self.result

    def set_location(self, loc):
        self.location = loc

    def send_request(self):
        url = ("https://maps.googleapis.com/maps/api/place/nearbysearch/"
                +   f"json?location={self.location}&key={GOOGLE_API_KEY}")
        req = requests.get(url)
        self.result = req.json()



