from masoniteorm.query import QueryBuilder


class SongPlayBuilder(QueryBuilder):

    def with_meta(self):
        return self.left_join("songs", "song_plays.song_id", "=", "songs.id") \
            .left_join("artists", "songs.artist_id", "=", "artists.id") \
            .left_join("albums", "songs.album_id", "=", "albums.id") \
            .left_join("genres", "songs.genre_id", "=", "genres.id") \
            .select(
                "songs.*",
                "artists.name as artist",
                "albums.title as album",
                "genres.name as genre",
                "song_plays.play_count",
                "song_plays.last_played_at",
                "song_plays.user_id",
                "song_plays.song_id"
            )
