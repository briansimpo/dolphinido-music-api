from masonite.controllers import Controller
from masonite.request import Request
from masonite.response import Response

from app.models import ShowPerformer


class ShowPerformersController(Controller):

    def delete(self, id, response: Response):
        performer = ShowPerformer.find(record_id=id)
        performer.delete()
        return response.json(payload={"message": "performer deleted"}, status=204)

    def store(self, request: Request, response: Response):
        show_id = request.input("show_id")
        artist_id = request.input("artist_id")

        performer = ShowPerformer.create({
            "show_id": show_id,
            "artist_id": artist_id
        })
        return response.json(performer.serialize())


