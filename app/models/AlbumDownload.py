from masoniteorm.models import Model
from masoniteorm.relationships import belongs_to
from app.builders import HasBuilder, AlbumDownloadBuilder


class AlbumDownload(Model, HasBuilder):
    __fillable__ = ['id', 'user_id', 'album_id', 'download_count', 'last_downloaded_at']

    def increment(self):
        count = self.download_count
        self.__setattr__("download_count", count+1)
        self.save()

    def get_builder(self):
        return self.new_builder(AlbumDownloadBuilder)

    @belongs_to('user_id', 'id')
    def user(self):
        from app.models.User import User
        return User

    @belongs_to('album_id', 'id')
    def album(self):
        from app.models.Album import Album
        return Album
