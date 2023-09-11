from datetime import datetime

from masonite.controllers import Controller
from masonite.request import Request
from masonite.response import Response

from app.models import AlbumDownload
from app.repositories import AlbumRepository, AlbumDownloadRepository


class AlbumDownloadsController(Controller):

    def __init__(self, album_repository: AlbumRepository, downloads_repository: AlbumDownloadRepository):
        self.album_repository = album_repository
        self.downloads_repository = downloads_repository

    def index(self, request: Request, response: Response):
        user = request.user()
        downloads = self.downloads_repository.get_downloads(user.id)
        return response.json(downloads.serialize())

    def store(self, id, request: Request, response: Response):
        user = request.user()
        album = self.album_repository.get_by_id(id)

        download_exists = self.downloads_repository.download_exists(user.id, album.id)

        if download_exists:
            download = self.downloads_repository.get_download(user.id, album.id)
            download.increment()
        else:
            AlbumDownload.create({
                "user_id": user.id,
                "album_id": album.id,
                "download_count": 1,
                "last_downloaded_at": datetime.timestamp()
            })

        return response.json(album.serialize())

