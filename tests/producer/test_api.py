from faker import Faker
from faker.providers import profile
from faker.providers import color
import requests
import json
from tests.commons.logger import get_logger

logger = get_logger('test_api.py')
fake = Faker()
fake.add_provider(profile)
fake.add_provider(color)

def test_producer():
    for i in range(1000): 
        simple = fake.simple_profile()
        logger.info(simple)
        logger.info(simple['username'])
        message = {
            "id" : 1,
            "text" : {
                "name" : simple['name'],
                "username" : simple['username'],
                "password" : fake.color_name(),
                "sex" : simple['sex'],
                "address" : simple['address'],
                "mail" : simple['mail'],
            }
        }
        logger.info(message)
        response = requests.post("http://127.0.0.1:8002/producer", data=json.dumps(message))
        logger.info(response.json())
        assert response.status_code == 200