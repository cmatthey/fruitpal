#  Coco Matthey
#  https://www.linkedin.com/in/coco-matthey/

import json
import requests
from app.services.feeddev import OVERHEADDATA

# TODO: parameterize the nightly feed
OVERHEADDATA_FILE = "OVERNIGHTFEED.txt"
OVERHEADDATA_URL = "https://localhost/api/feed"


class OverheadData:
    def __init__(self, mode="FILE"):
        # TODO: Use environment variable or other configurations
        if mode == "DEV":
            self.overheadData = OVERHEADDATA
        elif mode == "FILE":
            with open(OVERHEADDATA_FILE, "r") as overnightFile:
                self.overheadData = json.load(overnightFile)
        elif mode == "NETWORK":
            try:
                response = requests.get(OVERHEADDATA_URL)
                self.overheadData = response.json()
            # TODO: Use logger
            except Exception as e:
                print(e)
        else:
            raise Exception("Invalid mode")
