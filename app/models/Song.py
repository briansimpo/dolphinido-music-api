from masoniteorm.models import Model
from masoniteorm.scopes import UUIDPrimaryKeyMixin
from masoniteorm.relationships import belongs_to
from app.builders import HasBuilder, SongBuilder


class Song(Model, UUIDPrimaryKeyMixin, HasBuilder):

    __fillable__ = [
        'id',  'title', 'filepath', 'filehash', 'filesize', 'bitrate', 'duration', 'is_free', 'is_published', 
        'release_year', 'cover_image', 'lyrics', 'artist_id', 'genre_id', 'album_id'
    ]

    # derived attributes from SongBuilder
    __casts__ = {"downloads": "decimal", "plays": "decimal"}

    def publish(self):
        self.__setattr__('is_published', True)
        return self.save()

    def unpublish(self):
        self.__setattr__('is_published', False)
        return self.save()

    def get_builder(self):
        return self.new_builder(SongBuilder)

    @belongs_to('artist_id', 'id')
    def artist(self):
        from app.models.Artist import Artist
        return Artist

    @belongs_to('album_id', 'id')
    def album(self):
        from app.models.Album import Album
        return Album
    
    @belongs_to('genre_id', 'id')
    def genre(self):
        from app.models.Genre import Genre
        return Genre
    
   
