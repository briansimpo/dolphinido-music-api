from masoniteorm.models import Model
from masoniteorm.scopes import UUIDPrimaryKeyMixin
from masoniteorm.relationships import has_many


class Genre(Model, UUIDPrimaryKeyMixin):
    __fillable__ = ['id', 'name', 'slug']

    @has_many('genre_id', 'id')
    def songs(self):
        from app.models.Song import Song
        return Song

    def __str__(self) -> str:
        return self.name

