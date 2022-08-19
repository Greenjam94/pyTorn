from datetime import timezone
import datetime


class Faction(object):
    def __init__(self, TornApi):
        self.api = TornApi
        self.raw = self.api.get_faction()
        self.last_updated = datetime.datetime.now(timezone.utc)