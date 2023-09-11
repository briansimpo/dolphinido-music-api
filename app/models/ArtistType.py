from masoniteorm.models import Model
from masoniteorm.scopes import UUIDPrimaryKeyMixin
from masoniteorm.relationships import has_many


class ArtistType(Model, UUIDPrimaryKeyMixin):
    __fillable__ = ['id', 'name', 'slug']

    @has_many('artist_type_id', 'id')
    def artists(self):
        from app.models.Artist import Artist
        return Artist

    def __str__(self) -> str:
        return self.name

