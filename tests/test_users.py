from api.endpoints import Endpoints
from fixtures.fixtures import *

def test_get_users(api_client):

    response = api_client.get(Endpoints.USERS)

    assert response.status_code == 200
    #print(response.json())
    assert isinstance(response.json(), list)
    

def test_create_user(api_client):

    payload = {
        "name": "Neethu",
        "email": "neethu@test.com"
    }

    response = api_client.post(Endpoints.USERS, payload)
    #print(response.json())
    assert response.status_code in [200, 201]