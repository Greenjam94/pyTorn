from dotenv import load_dotenv
import os
load_dotenv()

from torn import TornApi
from torn.user import User


ta = TornApi(os.getenv('API_KEY'))
my = User(ta)
print(my.name)
print(my.attack_link())
print(my.raw)