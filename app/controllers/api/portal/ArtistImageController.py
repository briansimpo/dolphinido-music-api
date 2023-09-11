from masonite.controllers import Controller
from masonite.request import Request
from masonite.response import Response

from app.repositories import ArtistRepository
from app.services import ArtistImageService


class ArtistImageController(Controller):

    def __init__(self, artist_repository: ArtistRepository, image_service: ArtistImageService):
        self.artist_repository = artist_repository
        self.image_service = image_service

    def update(self, request: Request, response: Response):
        user = request.user()
        image = request.input("image")
        artist = self.artist_repository.get_by_id(user.id)
        self.image_service.update(artist, image)
        return response.json(artist.serialize())
