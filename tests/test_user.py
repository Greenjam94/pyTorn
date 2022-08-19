from pytest import fixture
from dotenv import load_dotenv
import os
load_dotenv()

from torn import TornApi
from torn.user import User

@fixture
def user_jsonkeys():
    # Responsible only for returning the test data
    # ToDo-Low: Add all available keys from User response
    return ['player_id', 'name', 'role', 'age', 'level', 'rank']

def test_user_get(user_jsonkeys):
    """
    Tests an AP call to get a user provided an API key"""

    ta = TornApi(os.getenv('API_KEY'))
    u = User(ta)
    response = u.raw

    assert response['player_id'] == 1692273
    assert set(user_jsonkeys).issubset(response.keys()), "All expected keys should be in the response"

    assert isinstance(response['states'], dict)
    assert isinstance(response['life'], dict)
    assert isinstance(response['life']['current'], int)
