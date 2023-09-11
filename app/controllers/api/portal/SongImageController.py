from masonite.controllers import Controller
from masonite.request import Request
from masonite.response import Response

from app.repositories import SongRepository
from app.services import SongImageService


class SongImageController(Controller):

    def __init__(self, song_repository: SongRepository, image_service: SongImageService):
        self.song_repository = song_repository
        self.image_service = image_service

    def update(self, id, request: Request, response: Response):
        image = request.input("cover_image")
        song = self.song_repository.get_by_id(id)
        self.image_service.update(song, image)
        return response.json(song.serialize())
