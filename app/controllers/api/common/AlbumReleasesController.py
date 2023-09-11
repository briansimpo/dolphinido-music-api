from masonite.controllers import Controller
from masonite.request import Request
from masonite.response import Response
from slugify import slugify

from app.models import AlbumRelease


class AlbumReleasesController(Controller):

    def index(self, response: Response):
        album_releases = AlbumRelease.all()
        return response.json(album_releases.serialize())

    def show(self, id, response: Response):
        album_release = AlbumRelease.find(record_id=id)
        return response.json(album_release.serialize())

    def store(self, request: Request, response: Response):
        name = request.input("name")
        slug = slugify(text=name, separator="_")
        album_release = AlbumRelease.create({
            "name": name,
            "slug": slug
        })
        return response.json(album_release.serialize())

    def update(self, id, request: Request, response: Response):
        name = request.input("name")
        slug = slugify(text=name, separator="_")
        album_release = AlbumRelease.find(record_id=id)
        album_release.update({
            "name": name,
            "slug": slug
        })
        return response.json(album_release.serialize())

    def destroy(self, id, response: Response):
        album_release = AlbumRelease.find(record_id=id)
        album_release.delete()
        return response.json(payload={"message": "record deleted"}, status=204)
