from masonite.controllers import Controller
from masonite.request import Request
from masonite.response import Response
from slugify import slugify

from app.models import Genre


class GenresController(Controller):

    def index(self, response: Response):
        genres = Genre.all()
        return response.json(genres.serialize())

    def show(self, id, response: Response):
        genre = Genre.find(record_id=id)
        return response.json(genre.serialize())

    def store(self, request: Request, response: Response):
        name = request.input("name")
        slug = slugify(text=name, separator="_")
        genre = Genre.create({
            "name": name,
            "slug": slug
        })
        return response.json(genre.serialize())

    def update(self, id, request: Request, response: Response):
        name = request.input("name")
        slug = slugify(text=name, separator="_")
        genre = Genre.find(record_id=id)
        genre.update({
            "name": name,
            "slug": slug
        })
        return response.json(genre.serialize())

    def destroy(self, id, response: Response):
        genre = Genre.find(record_id=id)
        genre.delete()
        return response.json(payload={"message": "record deleted"}, status=204)
