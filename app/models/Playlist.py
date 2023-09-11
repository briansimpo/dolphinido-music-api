from masoniteorm.models import Model
from masoniteorm.scopes import UUIDPrimaryKeyMixin
from masoniteorm.relationships import belongs_to, belongs_to_many


class Playlist(Model, UUIDPrimaryKeyMixin):
    __fillable__ = ['id', 'name', 'user_id']

    @belongs_to('user_id', 'id')
    def user(self):
        from app.models.User import User
        return User
    
    @belongs_to_many('playlist_id', 'song_id', 'id', 'id', 'playlist_songs')
    def songs(self):
        from app.models.Song import Song
        return Song

    def __str__(self) -> str:
        return self.name
