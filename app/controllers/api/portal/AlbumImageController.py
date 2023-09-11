from masonite.controllers import Controller
from masonite.request import Request
from masonite.response import Response

from app.repositories import AlbumRepository
from app.services import AlbumImageService


class AlbumImageController(Controller):

    def __init__(self, album_repository: AlbumRepository, image_service: AlbumImageService):
        self.album_repository = album_repository
        self.image_service = image_service

    def update(self, id, request: Request, response: Response):
        image = request.input("cover_image")
        album = self.album_repository.get_by_id(id)
        self.image_service.update(album, image)
        return response.json(album.serialize())

