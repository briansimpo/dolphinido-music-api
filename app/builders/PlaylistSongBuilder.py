from masoniteorm.query import QueryBuilder


class PlaylistSongBuilder(QueryBuilder):

    def with_meta(self):
        return self.left_join("songs", "playlist_songs.song_id", "=", "songs.id") \
            .left_join("artists", "songs.artist_id", "=", "artists.id") \
            .left_join("albums", "songs.album_id", "=", "albums.id") \
            .left_join("genres", "songs.genre_id", "=", "genres.id") \
            .select(
                "songs.*",
                "artists.name as artist",
                "albums.title as album",
                "genres.name as genre",
                "playlist_songs.song_id",
                "playlist_songs.playlist_id"
            )
