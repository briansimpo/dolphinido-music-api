from masoniteorm.query import QueryBuilder


class AlbumLikeBuilder(QueryBuilder):

    def with_meta(self):
        return self.left_join("albums", "album_likes.album_id", "=", "albums.id") \
            .left_join("artists", "albums.artist_id", "=", "artists.id") \
            .left_join("genres", "albums.genre_id", "=", "genres.id") \
            .left_join("album_releases", "albums.album_release_id", "=", "album_releases.id") \
            .select(
                "albums.*",
                "artists.name as artist",
                "genres.name as genre",
                "album_releases.name as album_release",
                "album_likes.user_id",
                "album_likes.album_id"
            )
