from masoniteorm.models import Model
from masoniteorm.relationships import belongs_to
from app.builders import HasBuilder, SongDownloadBuilder


class SongDownload(Model, HasBuilder):
    __fillable__ = ['id', 'user_id', 'song_id', 'download_count', 'last_downloaded_at']

    def increment(self):
        count = self.download_count
        self.__setattr__("download_count", count + 1)
        self.save()

    def get_builder(self):
        return self.new_builder(SongDownloadBuilder)

    @belongs_to('user_id', 'id')
    def user(self):
        from app.models.User import User
        return User

    @belongs_to('song_id', 'id')
    def song(self):
        from app.models.Song import Song
        return Song
