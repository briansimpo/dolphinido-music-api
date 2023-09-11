from masoniteorm.query import QueryBuilder


class AlbumDownloadBuilder(QueryBuilder):

    def with_meta(self):
        return self.left_join("albums", "album_downloads.album_id", "=", "albums.id") \
            .left_join("artists", "albums.artist_id", "=", "artists.id") \
            .left_join("genres", "albums.genre_id", "=", "genres.id") \
            .left_join("album_releases", "albums.album_release_id", "=", "album_releases.id") \
            .select(
                "albums.*",
                "artists.name as artist",
                "genres.name as genre",
                "album_releases.name as album_release",
                "album_downloads.download_count",
                "album_downloads.last_downloaded_at",
                "album_downloads.user_id",
                "album_downloads.album_id"
            )
