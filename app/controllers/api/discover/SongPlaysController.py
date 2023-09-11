from datetime import datetime

from masonite.controllers import Controller
from masonite.request import Request
from masonite.response import Response

from app.models import SongPlay
from app.repositories import SongRepository, SongPlayRepository


class SongPlaysController(Controller):

    def __init__(self, song_repository: SongRepository, plays_repository: SongPlayRepository):
        self.song_repository = song_repository
        self.plays_repository = plays_repository

    def index(self, request: Request, response: Response):
        user = request.user()
        plays = self.plays_repository.get_plays(user.id)
        return response.json(plays.serialize())

    def store(self, id, request: Request, response: Response):
        user = request.user()
        song = self.song_repository.get_by_id(id)

        play_exists = self.plays_repository.play_exists(user.id, song.id)

        if play_exists:
            play = self.plays_repository.get_play(user.id, song.id)
            play.increment()
        else:
            SongPlay.create({
                "user_id": user.id,
                "song_id": song.id,
                "play_count": 1,
                "last_played_at": datetime.timestamp()
            })

        return response.json(song.serialize())


