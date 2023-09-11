from masoniteorm.models import Model
from masoniteorm.scopes import UUIDPrimaryKeyMixin
from masoniteorm.relationships import belongs_to, has_many
from app.builders import HasBuilder, ArtistBuilder


class Artist(Model, UUIDPrimaryKeyMixin, HasBuilder):
    __fillable__ = [
        'id', 'name', 'birthday', 'country', 'city', 'bio', 'image', 'artist_type_id'
    ]

    @belongs_to('id', 'id')
    def user(self):
        from app.models import User
        return User
    
    @has_many('artist_id', 'id')
    def songs(self):
        from app.models.Song import Song
        return Song
    
    @has_many('artist_id', 'id')
    def albums(self):
        from app.models.Album import Album
        return Album

    @belongs_to('artist_type_id', 'id')
    def artist_type(self):
        from app.models import ArtistType
        return ArtistType
    
    def get_builder(self):
        return self.new_builder(ArtistBuilder)
    
    def __str__(self) -> str:
        return self.name

