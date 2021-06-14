import requests

GENDERIZE_API = "https://api.genderize.io"
AGIFY_API = "https://api.agify.io"


class AgifyAndGenderize:
    def __init__(self, name):
        self.param = {
            "name": name
        }

    def get_genderize(self):
        response = requests.get(url=GENDERIZE_API, params=self.param).json()
        return response["gender"]

    def get_agify(self):
        response = requests.get(url=AGIFY_API, params=self.param).json()
        return response["age"]
