from masonite.controllers import Controller
from masonite.request import Request
from masonite.response import Response
from app.repositories import SongRepository, AlbumRepository


class AlbumTracksController(Controller):
    def __init__(self, song_repository: SongRepository, album_repository: AlbumRepository):
        self.song_repository = song_repository
        self.album_repository = album_repository

    def delete(self, id, response: Response):
        song = self.song_repository.get_by_id(id)
        song.album_id = None
        song.save()
        return response.json(song.serialize())

    def store(self, request: Request, response: Response):
        album_id = request.input("album")
        song_id_list = request.input("songs")

        for song_id in song_id_list:
            song = self.song_repository.get_by_id(song_id)
            song.album_id = album_id
            song.save()
        return response.json({"data": song_id_list})


