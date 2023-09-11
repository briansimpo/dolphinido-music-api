from masonite.controllers import Controller
from masonite.request import Request
from masonite.response import Response

from app.models import SongLike
from app.repositories import SongRepository, SongLikeRepository


class SongLikesController(Controller):

    def __init__(self, song_repository: SongRepository, likes_repository: SongLikeRepository):
        self.song_repository = song_repository
        self.likes_repository = likes_repository

    def index(self, request: Request, response: Response):
        user = request.user()
        likes = self.likes_repository.get_likes(user.id)
        return response.json(likes.serialize())

    def store(self, id, request: Request, response: Response):
        user = request.user()
        song = self.song_repository.get_by_id(id)

        like_exists = self.likes_repository.like_exists(user.id, song.id)

        if not like_exists:
            SongLike.create({
                "user_id": user.id,
                "song_id": song.id
            })

        return response.json(song.serialize())

