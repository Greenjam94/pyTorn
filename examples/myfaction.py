from dotenv import load_dotenv
import os
load_dotenv()

from torn import TornApi

ta = TornApi(os.getenv('API_KEY'))
lol = ta.get_faction()

print(lol)
