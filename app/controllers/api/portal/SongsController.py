from masonite.controllers import Controller
from masonite.request import Request
from masonite.response import Response
from masonite.queues import Queue

from app.models import Song
from app.jobs import Fingerprint
from app.repositories import SongRepository
from app.services import SongFileService, SongImageService


class SongsController(Controller):

    def __init__(self, song_repository: SongRepository, file_service: SongFileService, image_service: SongImageService):
        self.song_repository = song_repository
        self.file_service = file_service
        self.image_service = image_service

    def index(self, request: Request, response: Response):
        user = request.user()
        songs = self.song_repository.get_by_artist(user.id)
        return response.json(songs.serialize())

    def show(self, id, response: Response):
        song = self.song_repository.get_by_id(id)
        return response.json(song.serialize())

    def store(self, request: Request, response: Response, queue: Queue):
        user = request.user()
        uploaded_file = request.input("song_file")
        uploaded_image = request.input("cover_image")

        song_file, song_hash = self.file_service.upload(uploaded_file)
        audio = self.song_repository.get_by_hash(song_hash)

        if audio:
            self.file_service.delete(song_file)
            return response.json({"message": "song already exists"}, 302)

        song = Song.create({
            "artist_id": user.id,
            "hash": song_hash,
            "title": request.input("title"),
            "release_date": request.input("release_date"),
            "album_id": request.input("album") or None,
            "genre_id": request.input("genre")        
        })

        self.file_service.store(song, song_file)
        self.image_service.store(song, uploaded_image)

        queue.push(Fingerprint(song.id))

        return response.json(song.serialize(), 201)

    def update(self, id, request: Request, response: Response):

        song = self.song_repository.get_by_id(id)

        song.update({
            "title": request.input("title"),
            "release_date": request.input("release_date"),
            "album_id": request.input("album") or None,
            "genre_id": request.input("genre")
        })
        return response.json(song.serialize())

    def destroy(self, id, response: Response):
        song = self.song_repository.get_by_id(id)
        old_file = song.file
        old_image = song.cover_image
        song.delete()
        self.file_service.delete(old_file)
        self.image_service.delete(old_image)
        return response.json(payload={"message": "song deleted"}, status=204)

    def publish(self, id, response: Response):
        song = self.song_repository.get_by_id(id)
        song.publish()
        return response.json(song.serialize())

    def unpublish(self, id, response: Response):
        song = self.song_repository.get_by_id(id)
        song.unpublish()
        return response.json(song.serialize())

    def unknown_album(self, request: Request, response: Response):
        user = request.user()
        songs = self.song_repository.get_unknown_album_by_artist(user.id)
        return response.json(songs.serialize())
