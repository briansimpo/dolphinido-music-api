from masonite.controllers import Controller
from masonite.request import Request
from masonite.response import Response

from app.models import AlbumLike
from app.repositories import AlbumRepository, AlbumLikeRepository


class AlbumLikesController(Controller):

    def __init__(self, album_repository: AlbumRepository, likes_repository: AlbumLikeRepository):
        self.album_repository = album_repository
        self.likes_repository = likes_repository

    def index(self, request: Request, response: Response):
        user = request.user()
        likes = self.likes_repository.get_likes(user.id)
        return response.json(likes.serialize())

    def store(self, id, request: Request, response: Response):
        user = request.user()
        album = self.album_repository.get_by_id(id)

        like_exists = self.likes_repository.like_exists(user.id, album.id)

        if not like_exists:
            AlbumLike.create({
                "user_id": user.id,
                "album_id": album.id
            })

        return response.json(album.serialize())

