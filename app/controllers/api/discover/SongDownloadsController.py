from datetime import datetime

from masonite.controllers import Controller
from masonite.request import Request
from masonite.response import Response

from app.models import SongDownload
from app.repositories import SongRepository, SongDownloadRepository


class SongDownloadsController(Controller):

    def __init__(self, song_repository: SongRepository, downloads_repository: SongDownloadRepository):
        self.song_repository = song_repository
        self.downloads_repository = downloads_repository

    def index(self, request: Request, response: Response):
        user = request.user()
        downloads = self.downloads_repository.get_downloads(user.id)
        return response.json(downloads.serialize())

    def store(self, id, request: Request, response: Response):
        user = request.user()
        song = self.song_repository.get_by_id(id)

        download_exists = self.downloads_repository.download_exists(user.id, song.id)

        if download_exists:
            download = self.downloads_repository.get_download(user.id, song.id)
            download.increment()
        else:
            SongDownload.create({
                "user_id": user.id,
                "song_id": song.id,
                "download_count": 1,
                "last_downloaded_at": datetime.timestamp()
            })

        return response.json(song.serialize())


