from masoniteorm.models import Model
from masoniteorm.relationships import belongs_to
from app.builders import HasBuilder, SongLikeBuilder


class SongLike(Model, HasBuilder):
    __fillable__ = ['id', 'user_id', 'song_id']

    def get_builder(self):
        return self.new_builder(SongLikeBuilder)

    @belongs_to('user_id', 'id')
    def user(self):
        from app.models.User import User
        return User

    @belongs_to('song_id', 'id')
    def song(self):
        from app.models.Song import Song
        return Song
