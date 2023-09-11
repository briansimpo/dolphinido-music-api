from masoniteorm.models import Model
from masoniteorm.scopes import UUIDPrimaryKeyMixin
from masoniteorm.scopes import SoftDeletesMixin
from masonite.authentication import Authenticates
from masonite.api.authentication import AuthenticatesTokens
from masoniteorm.relationships import has_one, has_many


class User(Model, UUIDPrimaryKeyMixin, SoftDeletesMixin, Authenticates, AuthenticatesTokens):
    __TOKEN_COLUMN__ = "api_token"
    __fillable__ = ["id", "name", "email", "password", "is_artist", "is_fan", "is_admin", "image"]
    __hidden__ = ["password"]
    __auth__ = "email"

    def become_artist(self):
        self.is_artist = True
        self.is_fan = False
        self.save()

    @has_one('id', 'id')
    def artist(self):
        from app.models.Artist import Artist
        return Artist

    @has_many('id', 'user_id')
    def playlists(self):
        from app.models.Playlist import Playlist
        return Playlist

    @has_many('id', 'user_id')
    def song_downloads(self):
        from app.models.SongDownload import SongDownload
        return SongDownload

    @has_many('id', 'user_id')
    def song_plays(self):
        from app.models.SongPlay import SongPlay
        return SongPlay

    @has_many('id', 'user_id')
    def song_likes(self):
        from app.models.SongLike import SongLike
        return SongLike

    @has_many('id', 'user_id')
    def followings(self):
        from app.models.Following import Following
        return Following
        
    @has_many('id', 'user_id')
    def album_downloads(self):
        from app.models.AlbumDownload import AlbumDownload
        return AlbumDownload
    
    @has_many('id', 'user_id')
    def album_likes(self):
        from app.models.AlbumLike import AlbumLike
        return AlbumLike
