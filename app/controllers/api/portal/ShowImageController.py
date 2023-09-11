from masonite.controllers import Controller
from masonite.request import Request
from masonite.response import Response

from app.repositories import ShowRepository
from app.services import ShowImageService


class ShowImageController(Controller):

    def __init__(self, show_repository: ShowRepository, image_service: ShowImageService):
        self.show_repository = show_repository
        self.image_service = image_service

    def update(self, id, request: Request, response: Response):
        image = request.input("cover_image")
        show = self.show_repository.get_by_id(id)
        self.image_service.update(show, image)
        return response.json(show.serialize())

