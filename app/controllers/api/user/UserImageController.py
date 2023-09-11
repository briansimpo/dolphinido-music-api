from masonite.controllers import Controller
from masonite.request import Request
from masonite.response import Response

from app.services import UserImageService


class UserImageController(Controller):

    def __init__(self, image_service: UserImageService):
        self.image_service = image_service

    def update(self, request: Request, response: Response):
        user = request.user()
        image = request.input("profile_image")
        self.image_service.update(user, image)
        return response.json(user.serialize())
