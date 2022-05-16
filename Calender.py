import requests

class calenderApi:
    def __init__(self, category=10, amount=1): 
     self.url='http://calapi.inadiutorium.cz/api/v0/en/calendars/default/today'

    def get(self):
        r=requests.get(self.url)
        response=r.json()
        return response