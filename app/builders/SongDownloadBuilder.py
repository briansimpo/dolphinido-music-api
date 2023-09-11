from masoniteorm.query import QueryBuilder


class SongDownloadBuilder(QueryBuilder):

    def with_meta(self):
        return self.left_join("songs", "song_downloads.song_id", "=", "songs.id") \
            .left_join("artists", "songs.artist_id", "=", "artists.id") \
            .left_join("albums", "songs.album_id", "=", "albums.id") \
            .left_join("genres", "songs.genre_id", "=", "genres.id") \
            .select(
                "songs.*",
                "artists.name as artist",
                "albums.title as album",
                "genres.name as genre",
                "song_downloads.download_count",
                "song_downloads.last_downloaded_at",
                "song_downloads.user_id",
                "song_downloads.song_id"
            )
