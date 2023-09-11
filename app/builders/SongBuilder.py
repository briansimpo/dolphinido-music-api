from masoniteorm.query import QueryBuilder


class SongBuilder(QueryBuilder):

    def with_meta(self):
        return self.left_join("artists", "songs.artist_id", "=", "artists.id") \
            .left_join("albums", "songs.album_id", "=", "albums.id") \
            .left_join("genres", "songs.genre_id", "=", "genres.id") \
            .left_join("song_downloads", "songs.id", "=", "song_downloads.song_id") \
            .left_join("song_plays", "songs.id", "=", "song_plays.song_id") \
            .left_join("song_likes", "songs.id", "=", "song_likes.song_id") \
            .sum("song_downloads.download_count as downloads") \
            .sum("song_plays.play_count as plays") \
            .count("song_likes.id as likes") \
            .group_by("songs.id") \
            .select(
                "songs.*",
                "artists.name as artist",
                "albums.title as album",
                "genres.name as genre"
            )
