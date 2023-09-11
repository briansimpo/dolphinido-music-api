from masoniteorm.models import Model
from masoniteorm.scopes import UUIDPrimaryKeyMixin
from masoniteorm.relationships import has_many


class AlbumRelease(Model, UUIDPrimaryKeyMixin):
    __fillable__ = ['id', 'name', 'slug']

    @has_many('album_release_id', 'id')
    def albums(self):
        from app.models.Album import Album
        return Album

    def __str__(self) -> str:
        return self.name
