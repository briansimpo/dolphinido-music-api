from masonite.request import Request
from masonite.response import Response
from masonite.controllers import Controller


class UserController(Controller):

    def show(self, request: Request, response: Response):
        user = request.user()
        return response.json(user.serialize())

