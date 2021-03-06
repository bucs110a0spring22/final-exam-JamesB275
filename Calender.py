import requests

class calenderApi:
    def __init__(self):
      '''
      Stores API url in Class
      :params=None
      :returns=None
      '''
      self.api_url='http://calapi.inadiutorium.cz/api/v0/en/calendars/default/today'

    def get(self):
        '''
        This method pulls the data from the API
        :params=None
        :returns=response
        '''
        r=requests.get(self.api_url)
        response=r.json()
        return response