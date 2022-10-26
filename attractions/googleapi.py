import requests

from moreaboutattractions.settings import GOOGLE_API_KEY


class GoogleApi():
    location = {
        'latitude': "",
        'longitude': ""
    }
    result = ""

    def __init__(self, latitude, longitude):
        self.location['latitude'] = latitude
        self.location['longitude'] = longitude

    def __str__(self):
        return self.result

    def send_request(self):
        url = ("https://maps.googleapis.com/maps/api/place/nearbysearch/"
                +   f"json?location={self.location}&key={GOOGLE_API_KEY}")
        req = requests.get(url)
        self.result = req.json()
        return self.result

    def mock_api(self):
        attractions = {
            '001': {
                'name': "Verona Arena",
                'type': "Arena",
                'stars': "4,7",
                'reviews': "120142",
                'price': ""
            },
            '002': {
                'name': "Castelvecchio Museum",
                'type': "Museum",
                'stars': "4,6",
                'reviews': "13337",
                'price': ""
            },
            '003': {
                'name': "Piazza delle Erbe",
                'type': "Tourist attraction",
                'stars': "4,7",
                'reviews': "11216",
                'price': "€€"
            }
        }

        return attractions