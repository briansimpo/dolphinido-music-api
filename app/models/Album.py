import datetime
from masoniteorm.models import Model
from masoniteorm.scopes import UUIDPrimaryKeyMixin
from masoniteorm.relationships import belongs_to
from masoniteorm.relationships import has_many
from app.builders import HasBuilder, AlbumBuilder


class Album(Model, UUIDPrimaryKeyMixin, HasBuilder):
    __fillable__ = [
        'id',  'title', 'is_free', 'is_published', 'release_date', 'cover_image',
        'artist_id', 'genre_id', 'album_release_id'
    ]

    __dates__ = ["release_date"]

    # derived attributes from AlbumBuilder
    __casts__ = {"downloads": "decimal"}

    def publish(self):
        self.__setattr__('is_published', True)
        return self.save()

    def unpublish(self):
        self.__setattr__('is_published', False)
        return self.save()

    def get_builder(self):
        return self.new_builder(AlbumBuilder)

    def total_tracks(self):
        from app.models.Song import Song
        return Song.where('album_id', self.id).count()
    
    def total_duration(self):
        duration = 0
        if self.has_tracks():
            for track in self.songs:
                duration += track.duration
        return duration

    def has_tracks(self):
        return self.total_tracks() > 0

    @staticmethod
    def get_by_artist(artist_id):
        return Album.where("artist_id", artist_id).get()

    @belongs_to('artist_id', 'id')
    def artist(self):
        from app.models.Artist import Artist
        return Artist

    @belongs_to('genre_id', 'id')
    def genre(self):
        from app.models.Genre import Genre
        return Genre
    
    @belongs_to('album_release_id', 'id')
    def album_release(self):
        from app.models.AlbumRelease import AlbumRelease
        return AlbumRelease
    
    @has_many('id', 'album_id')
    def songs(self):
        from app.models.Song import Song
        return Song

    def __str__(self) -> str:
        return self.title
