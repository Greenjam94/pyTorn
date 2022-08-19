from torn import TornApi
from torn.user import User

API_KEY = 'oops'

ta = TornApi(API_KEY)
lol = ta.get_faction()

print(lol)
