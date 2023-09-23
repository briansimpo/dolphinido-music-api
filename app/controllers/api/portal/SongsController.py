from masonite.controllers import Controller
from masonite.request import Request
from masonite.response import Response
from masonite.queues import Queue

from app.controllers.PaginatorMixin import PaginatorMixin
from app.repositories import SongRepository
from app.jobs import CreateAudioFingerprint, DeleteAudioFingerprint
from app.services import SongFileService, SongImageService
from app.models import Song

class SongsController(Controller, PaginatorMixin):

    def __init__(self, song_repository: SongRepository, file_service: SongFileService, image_service: SongImageService):
        self.song_repository = song_repository
        self.file_service = file_service
        self.image_service = image_service

    def index(self, request: Request, response: Response):
        try:
            user = request.user()
            per_page, page = self.paginator(request)
            songs = self.song_repository.get_by_artist(user.id, per_page, page)
            return response.json(songs.serialize())
        except:
            return response.json({})

    def show(self, id, response: Response):
        song = self.song_repository.get_by_id(id)
        return response.json(song.serialize())

    def store(self, request: Request, response: Response, queue: Queue):
        user = request.user()
        uploaded_file = request.input("song_file")

        file_path = self.file_service.upload_file(uploaded_file)
        file_hash = self.file_service.get_file_hash(file_path)
        audio = self.song_repository.get_by_filehash(file_hash)

        if audio:
            self.file_service.delete(file_path)
            return response.json({"message": "song already exists"}, 302)

        song = Song.create({
            "title": request.input("title"),
            "filepath": file_path,
            "filehash": file_hash,
            "artist_id": user.id        
        })

        self.image_service.default(song)
        self.file_service.store(song, file_path)

        # create_fingerprint = CreateAudioFingerprint(song)
        # queue.push(create_fingerprint)

        return response.json(song.serialize(), 201)

    def update(self, id, request: Request, response: Response):

        song = self.song_repository.get_by_id(id)

        song.update({
            "title": request.input("title"),
            "release_year": request.input("release_year"),
            "album_id": request.input("album") or None,
            "genre_id": request.input("genre")
        })
        return response.json(song.serialize())

    def destroy(self, id, response: Response, queue: Queue):
        song = self.song_repository.get_by_id(id)
        old_file = song.filepath
        old_image = song.cover_image
        song.delete()

        self.file_service.delete(old_file)
        self.image_service.delete(old_image)

        # delete_fingerprint = DeleteAudioFingerprint(song)
        # queue.push(delete_fingerprint)

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
