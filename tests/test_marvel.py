from src.marvel import Marvel
import json
import requests
from requests_mock.contrib import fixture
import testtools

class TestMarvel(testtools.TestCase):
    TEST_URL = "https://gateway.marvel.com/v1/public/characters"

    def setUp(self):
        super(TestMarvel, self).setUp()
        self.requests_mock = self.useFixture(fixture.Fixture())

    def test_hashed_key(self):
        client = Marvel()
        results  = client.create_hashed_key()
        assert results is not None 
        
    def test_get(self):
        with open("tests/fixtures/characters.json", "r") as file:
            data = json.load(file)
        client = Marvel()
        self.requests_mock.register_uri("GET",
            f"{client.URL}/v1/public/characters{client.query_string}", json=data)
        results = client.testing()
        assert results is not None
