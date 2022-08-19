from torn import TornApi
from torn.user import User

API_KEY = 'Yry4HDWt6aRSIKmy'

ta = TornApi(API_KEY)
lol = ta.get_faction()

print(lol)