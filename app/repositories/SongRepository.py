from .Repository import Repository
from .WorkFilterMixin import WorkFilterMixin


class SongRepository(Repository, WorkFilterMixin):

    def get_by_filehash(self, hash: str):
        return self.query().with_meta()\
            .where("songs.filehash", hash)\
            .first()
    
    def get_by_filepath(self, file_path: str):
        return self.query().with_meta()\
            .where("songs.filepath", file_path)\
            .first()

    def get_played_by_user_recently(self, user_id, limit: int = 20):
        return self.query().with_meta() \
            .left_join("song_plays", "songs.id", "=", "song_plays.song_id") \
            .where("song_plays.user_id", user_id) \
            .order_by("song_plays.last_played_at", "DESC") \
            .limit(limit).get()

    def get_most_played_by_user(self, user_id, limit: int = 20):
        return self.query().with_meta() \
            .left_join("song_plays", "songs.id", "=", "song_plays.song_id") \
            .where("song_plays.user_id", user_id) \
            .order_by("song_plays.play_count", "DESC") \
            .limit(limit).get()

    def get_most_downloaded_by_user(self, user_id, limit: int = 20):
        return self.query() \
            .left_join("song_downloads", "songs.id", "=", "song_downloads.song_id") \
            .where("song_downloads.user_id", user_id) \
            .order_by("song_downloads.download_count", "DESC") \
            .limit(limit).get()

    def get_by_album(self, album_id):
        return self.query().with_meta()\
            .where("songs.album_id", album_id)\
            .get()

    def get_by_artist(self, artist_id, limit: int = 20):
        return self.query().with_meta()\
            .where("songs.artist_id", artist_id)\
            .paginate(limit)

    def get_by_playlist(self, playlist_id):
        return self.query()\
            .left_join("playlist_songs", "songs.id", "=", "playlist_songs.song_id")\
            .left_join("playlists", "playlists.id", "=", "playlist_songs.playlist_id")\
            .where("playlists.id", playlist_id)\
            .order_by("songs.title").get()

    def get_unknown_album(self, limit: int = 20):
        return self.query().with_meta()\
            .where_null("songs.album_id")\
            .paginate(limit)

    def get_unknown_album_by_artist(self, artist_id):
        return self.query().with_meta()\
            .where("songs.artist_id", artist_id)\
            .where_null("songs.album_id")\
            .get()

    def get_most_played(self, limit: int = 20):
        return self.query().with_meta() \
            .left_join("song_plays", "songs.id", "=", "song_plays.song_id") \
            .group_by("songs.id") \
            .order_by("song_plays.play_count", "DESC") \
            .limit(limit).get()

    def get_most_downloaded(self, limit: int = 20):
        return self.query() \
            .left_join("song_downloads", "songs.id", "=", "song_downloads.song_id") \
            .group_by("songs.id") \
            .order_by("song_downloads.download_count", "DESC") \
            .limit(limit).get()

    def count_by_artist(self, artist_id):
        return self.query() \
            .where("songs.artist_id", artist_id) \
            .count()