from src.marvel import Marvel


class TestMarvel:

    def test_hashed_key(self):
        client = Marvel()
        results  = client.create_hashed_key()
        assert results is not None 

        