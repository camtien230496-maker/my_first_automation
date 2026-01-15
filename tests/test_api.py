import requests
from utils.config_reader import ConfigReader
from utils.api_helper import ApiHelper
import pytest

@pytest.mark.api
class TestApi:
    def test_get_endpoint(self):
        self.api = ApiHelper(ConfigReader.get_api_url)
        resp = self.api.get("users/1")
        print(f'response trả về là {resp}')
        
        email = resp.get("email")
        assert email == "Sincere@april.biz"
        
