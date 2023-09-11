from masoniteorm.models import Model
from masoniteorm.relationships import belongs_to
from app.builders import HasBuilder, PlaylistSongBuilder


class PlaylistSong(Model, HasBuilder):
    __fillable__ = ['id', 'playlist_id', 'song_id']

    def get_builder(self):
        return self.new_builder(PlaylistSongBuilder)

    @belongs_to('playlist_id', 'id')
    def playlist(self):
        from app.models.Playlist import Playlist
        return Playlist
    
    @belongs_to('song_id', 'id')
    def song(self):
        from app.models.Song import Song
        return Song

