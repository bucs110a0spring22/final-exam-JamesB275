import requests

class holidayApi:
    def __init__(self, category=10, amount=1): 
     self.url='https://isdayoff.ru/today?tz=America/New_York'

    def get(self):
        r=requests.get(self.url)
        response=r.json()
        return response