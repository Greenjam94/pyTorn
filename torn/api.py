import requests
import json

from .errors import *
from .urls import *
from .storage import *

class TornApi:
    def __init__(self, torn_api_key=None, db_file='sqlite.db'):

        # Attempt to read from exisiting sqlite db table, else create database tables
        try:
            create_connection(db_file)
            key_from_db = sqlite_query(db_file, "SELECT value, acces_level, player_id FROM keys LIMIT 1;")
        except:
            create_faction_table(db_file)
            create_users_table(db_file)
            create_keys_table(db_file)

        # Set instance variables
        self.api_key = torn_api_key if torn_api_key else key_from_db[0]
        self.db_file = db_file
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
    