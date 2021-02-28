import os
import hashlib 
import time

class Marvel:
    def __init__(self):
        self.private_key = os.environ.get("MARVEL_PUBLIC")
        self.public_key = os.environ.get("MARVEL_PRIVATE")
        self.ts = time.time()
        self.key_hashed = self.create_hashed_key()

    def create_hashed_key(self):
        """ https://developer.marvel.com/documentation/authorization """
        hashable = f"{self.ts}{self.private_key}{self.public_key}"
        return hashlib.md5(hashable.encode()).hexdigest()


    def  get_artists_works(self, artist):
        """ get the works of an artist """

    def get_writers_works(self, writer):
        """ get the works of a writer """

    def get_other_books_from_artist_and_writer(self, book):
        """ use the book to get more info """