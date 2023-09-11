from masonite.controllers import Controller
from masonite.response import Response

from app.models import Genre


class GenresController(Controller):

    def index(self, response: Response):
        genres = Genre.all()
        return response.json(genres.serialize())

    def show(self, id, response: Response):
        genre = Genre.find(record_id=id)
        return response.json(genre.serialize())
