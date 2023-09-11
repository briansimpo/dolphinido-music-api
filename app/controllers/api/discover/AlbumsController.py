from masonite.controllers import Controller
from masonite.response import Response

from app.repositories import AlbumRepository


class AlbumsController(Controller):

    def __init__(self, album_repository: AlbumRepository):
        self.album_repository = album_repository

    def index(self, response: Response):
        albums = self.album_repository.get_for_free()
        return response.json(albums.serialize())

    def show(self, id, response: Response):
        album = self.album_repository.get_by_id(id)
        return response.json(album.serialize())

