from masonite.controllers import Controller
from masonite.response import Response

from app.repositories import SongRepository


class SongsController(Controller):

    def __init__(self, song_repository: SongRepository):
        self.song_repository = song_repository

    def index(self, response: Response):
        songs = self.song_repository.get_for_free()
        return response.json(songs.serialize())

    def show(self, id, response: Response):
        song = self.song_repository.get_by_id(id)
        return response.json(song.serialize())
