import requests
import json

from .errors import *
from .urls import *

class TornApi:
    def __init__(self, torn_api_key):
        self.api_key = torn_api_key
        self.urls = urls()
        self.session = requests.Session()
        self.session.params = {}
        self.session.params['key'] = self.api_key

        if self.api_key is None:
            raise APIKeyMissingError(
                "All API calls require a Torn API key. See"
                "https://www.torn.com/preferences.php#tab=api"
                "to create a key for this python package."
            )

    def __get_data(self, url):
        response = self.session.get(url)
        json = response.json()

        if set(['error']).issubset(json.keys()):
            raise parseErrorCode(json['error']['code'])
        
        return json

    def get_user(self, player_id='', fields=''):
        return self.__get_data(self.urls.get_user().format(id=player_id, fields=fields))
    
    def get_property(self, property_id='', fields=''):
        return self.__get_data(self.urls.get_property().format(id=property_id, fields=fields))

    def get_faction(self, faction_id='', fields=''):
        return self.__get_data(self.urls.get_faction().format(id=faction_id, fields=fields))
    
    def get_company(self, company_id='', fields=''):
        return self.__get_data(self.urls.get_company().format(id=company_id, fields=fields))
    
    def get_market(self, item_id='', fields=''):
        return self.__get_data(self.urls.get_market().format(id=item_id, fields=fields))
    
    def get_generic(self, id='', fields=''):
        return self.__get_data(self.urls.get_generic().format(id=id, fields=fields))
    