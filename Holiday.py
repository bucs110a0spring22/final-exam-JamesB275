import requests

class holidayApi:
    def __init__(self):
     '''
     Stores API url in Class
     :params=None
     :returns=None
     '''
     self.url='https://isdayoff.ru/today?tz=America/New_York'

    def get(self):
        '''
        This method pulls the data from the API
        :params=None
        :returns=response
        '''
        r=requests.get(self.url)
        response=r.json()
        return response