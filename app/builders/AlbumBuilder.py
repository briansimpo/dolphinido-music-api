from masoniteorm.query import QueryBuilder


class AlbumBuilder(QueryBuilder):

    def with_meta(self):
        return self.left_join("artists", "albums.artist_id", "=", "artists.id") \
            .left_join("genres", "albums.genre_id", "=", "genres.id") \
            .left_join("album_releases", "albums.album_release_id", "=", "album_releases.id") \
            .left_join("album_downloads", "albums.id", "=", "album_downloads.album_id") \
            .left_join("album_likes", "albums.id", "=", "album_likes.album_id") \
            .sum("album_downloads.download_count as downloads") \
            .count("album_likes.id as likes") \
            .group_by("albums.id") \
            .select(
                "albums.*",
                "artists.name as artist",
                "genres.name as genre",
                "album_releases.name as album_release"
            )
