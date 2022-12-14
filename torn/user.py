from datetime import timezone
import datetime

from .urls import *
from .storage import create_connection, insert_user

class User(object):
    def __init__(self, TornApi, player_id=''):
        self.api = TornApi
        self.raw = self.api.get_user(player_id)
        self.last_updated = datetime.datetime.now(timezone.utc)

        # Json "parsing"
        self.rank = self.raw['rank']
        self.level = self.raw['level']
        self.property = self.raw['property']
        self.property_id = self.raw['property_id']
        self.signup = self.raw['signup']
        self.awards = self.raw['awards']
        self.friends = self.raw['friends']
        self.enemies = self.raw['enemies']
        self.forum_posts = self.raw['forum_posts']
        self.karma = self.raw['karma']
        self.age = self.raw['age']
        self.role = self.raw['role']
        self.donator = self.raw['donator']
        self.player_id = self.raw['player_id']
        self.name = self.raw['name']
        self.competition = self.raw['competition']
        self.revivable = self.raw['revivable']
        self.life = self.raw['life']
        self.state = self.raw['status']['state']
        self.status = self.raw['status']
        self.job = self.raw['job']
        self.faction = self.raw['faction']
        self.married = self.raw['married']
        self.icons = self.raw['basicicons']
        self.states = self.raw['states']
        self.last_action = self.raw['last_action']

        # Store user record to sqlite database
        conn = create_connection(self.api.db_file)
        user_dict = [self.player_id, self.level, self.age, self.donator, self.name,
            self.revivable, self.life['current'], self.life['maximum'],
            self.life['fulltime'], self.state, self.status['description'],
            self.status['until'], self.faction['faction_id'], self.states['hospital_timestamp'],
            self.states['jail_timestamp'], self.last_action['status'], self.last_action['timestamp']]
        insert_user(conn, user_dict)

    def attack_link(self):
        return urls().get_attack().format(target=self.player_id)
    
    def until_okay(self):
        now = datetime.datetime.now(timezone.utc)
        if self.state == "Okay":
            return now
        elif self.state == "Hospital":
            timestamp = self.status['until']
            until = datetime.datetime.fromtimestamp(timestamp)
            return until
        elif self.state == "Traveling":
            return -1
        return -1