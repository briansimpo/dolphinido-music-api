from .Repository import Repository
from .WorkFilterMixin import WorkFilterMixin


class AlbumRepository(Repository, WorkFilterMixin):

    def get_most_played_by_user(self, user_id, limit: int = 20):

        return self.query().with_meta()\
            .left_join("songs", "albums.id", "=", "songs.album_id") \
            .left_join("song_plays", "songs.id", "=", "song_plays.song_id")\
            .where("song_plays.user_id", user_id)\
            .order_by("song_plays.play_count", "DESC")\
            .limit(limit)\
            .get()

    def get_most_downloaded_by_user(self, user_id, limit: int = 20):

        return self.query().with_meta() \
            .left_join("songs", "albums.id", "=", "songs.album_id") \
            .left_join("song_downloads", "songs.id", "=", "song_downloads.song_id") \
            .where("song_downloads.user_id", user_id) \
            .order_by("song_downloads.download_count", "DESC") \
            .limit(limit) \
            .get()

    def get_most_played(self, limit: int = 20):

        return self.query().with_meta()\
            .left_join("songs", "albums.id", "=", "songs.album_id") \
            .left_join("song_plays", "songs.id", "=", "song_plays.song_id")\
            .group_by("albums.id")\
            .order_by("song_plays.play_count", "DESC")\
            .limit(limit)\
            .get()

    def get_most_downloaded(self, limit: int = 20):

        return self.query().with_meta() \
            .left_join("songs", "albums.id", "=", "songs.album_id") \
            .left_join("song_downloads", "songs.id", "=", "song_downloads.song_id") \
            .group_by("albums.id") \
            .order_by("song_downloads.download_count", "DESC") \
            .limit(limit) \
            .get()

    def get_by_artist(self, artist_id, limit: int = 20):
        return self.query().with_meta()\
            .where("albums.artist_id", artist_id)\
            .get()
    
    def count_by_artist(self, artist_id):
        return self.query().where("albums.artist_id", artist_id).count()