from masonite.controllers import Controller
from masonite.request import Request
from masonite.response import Response
from slugify import slugify

from app.models import ArtistType


class ArtistTypesController(Controller):

    def index(self, response: Response):
        artist_types =ArtistType.all()
        return response.json(artist_types.serialize())

    def show(self, id, response: Response):
        artist_type = ArtistType.find(record_id=id)
        return response.json(artist_type.serialize())

    def store(self, request: Request, response: Response):
        name = request.input("name")
        slug = slugify(text=name, separator="_")
        artist_type = ArtistType.create({
            "name": name,
            "slug": slug
        })
        return response.json(artist_type.serialize())

    def update(self, id, request: Request, response: Response):
        name = request.input("name")
        slug = slugify(text=name, separator="_")
        artist_type = ArtistType.find(record_id=id)
        artist_type.update({
            "name": name,
            "slug": slug
        })
        return response.json(artist_type.serialize())

    def destroy(self, id, response: Response):
        artist_type = ArtistType.find(record_id=id)
        artist_type.delete()
        return response.json(payload={"message": "record deleted"}, status=204)
