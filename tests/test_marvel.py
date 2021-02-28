from src.marvel import Marvel
import json
from requests_mock.contrib import fixture
import testtools

class TestMarvel(testtools.TestCase):
    TEST_URL = "https://gateway.marvel.com/v1/public/characters"

    def setUp(self):
        super(TestMarvel, self).setUp()

    def test_hashed_key(self):
        client = Marvel()
        results  = client.create_hashed_key()
        assert results is not None     
        
    def test_get(self):
        self.requests_mock = self.useFixture(fixture.Fixture())
        with open("tests/fixtures/characters.json", "r") as file:
            data = json.load(file)
        client = Marvel()
        self.requests_mock.register_uri("GET",
            f"{client.URL}/v1/public/characters{client.query_string}", json=data)
        results = client.testing()
        assert results is not None

    def test_get_creator_id(self):
        self.requests_mock = self.useFixture(fixture.Fixture())
        with open("tests/fixtures/creator.json", "r") as file:
            data = json.load(file)
        client = Marvel()
        creator_name_first = "John"
        creator_name_last  = "Romita"
        suffix = "Jr."
        self.requests_mock.register_uri("GET",
            f"{client.URL}/v1/public/creators{client.query_string}&firstName={creator_name_first}&lastName={creator_name_last}&limit=1", json=data)
        
        results = client.get_creator_id(
            creator_name_first,
            creator_name_last,
            suffix
        )
        assert results == 55555