import os
import hashlib
import time
import requests
from dotenv import load_dotenv
load_dotenv()


class Marvel:
    URL = "https://gateway.marvel.com"

    def __init__(self):
        self.private_key = os.environ.get("MARVEL_PRIVATE")
        self.public_key = os.environ.get("MARVEL_PUBLIC")
        self.ts = int(time.time())
        self.key_hashed = self.create_hashed_key()
        self.query_string = f"?ts={self.ts}&apikey={self.public_key}&hash={self.key_hashed}"

    def create_hashed_key(self):
        """ https://developer.marvel.com/documentation/authorization """
        hashable = f"{self.ts}{self.private_key}{self.public_key}"
        return hashlib.md5(hashable.encode()).hexdigest()

    def testing(self):
        return requests.get(f"{self.URL}/v1/public/characters{self.query_string}").json()

    def get_artists_works(self, artist):
        """ get the works of an artist """

    def get_writers_works(self, writer):
        """ get the works of a writer """

    def get_other_books_from_artist_and_writer(self, book):
        """ use the book to get more info """


if __name__ == "__main__":
    client = Marvel()
    results = client.testing()
    print(results)
