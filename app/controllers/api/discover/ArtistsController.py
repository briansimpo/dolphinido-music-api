from masonite.controllers import Controller
from masonite.response import Response

from app.repositories import ArtistRepository


class ArtistsController(Controller):

    def __init__(self, artist_repository: ArtistRepository):
        self.artist_repository = artist_repository

    def index(self, response: Response):
        artists = self.artist_repository.get_all()
        return response.json(artists.serialize())

    def show(self, id, response: Response):
        artist = self.artist_repository.get_by_id(id)
        return response.json(artist.serialize())
