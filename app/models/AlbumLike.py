from masoniteorm.models import Model
from masoniteorm.relationships import belongs_to
from app.builders import HasBuilder, AlbumLikeBuilder


class AlbumLike(Model, HasBuilder):
    __fillable__ = ['id', 'user_id', 'album_id']

    def get_builder(self):
        return self.new_builder(AlbumLikeBuilder)

    @belongs_to('user_id', 'id')
    def user(self):
        from app.models.User import User
        return User

    @belongs_to('album_id', 'id')
    def album(self):
        from app.models.Album import Album
        return Album
