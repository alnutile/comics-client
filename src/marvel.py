import os
import hashlib
import time
import requests
import urllib.parse
import  json
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

    def get_creator_id(self, creator_name_first, creator_name_last, suffix=None):
        """ get just one id from name and return just the id"""
        creator_name_first = urllib.parse.quote(creator_name_first)
        creator_name_last = urllib.parse.quote(creator_name_last)
        results = requests.get(
            f"{self.URL}/v1/public/creators{self.query_string}&firstName={creator_name_first}&lastName={creator_name_last}&limit=1").json()
        
        if len(results['data']['results']) > 0: 
            return results['data']['results'][0]['id']
        
        return False

    def get_comic_by_name(self, comic_name):
        """ use name to find the commic info """
        comic_name = urllib.parse.quote(comic_name)
        results = requests.get(
            f"{self.URL}/v1/public/comics{self.query_string}&titleStartsWith={comic_name}&limit=10").json()
        
        with open("tests/fixtures/comics.json", "w") as file:
            json.dump(results, file)
            
        return results

    def get_artists_works(self, artist):
        """ get the works of an artist """
        creators = urllib.parse.quote(artist)
        return requests.get(f"{self.URL}/v1/public/comics{self.query_string}&creators={creators}").json()

    def get_writers_works(self, writer):
        """ get the works of a writer """

    def get_other_books_from_artist_and_writer(self, book):
        """ use the book to get more info """


if __name__ == "__main__":
    client = Marvel()
    results = client.get_artists_works("romita")
    with open("tests/fixtures/artists.json", "w") as file:
        json.dump(results, file)
    print(results)
