
from app.filters import Filter


class SongFilter(Filter):
    
    def __init__(self) -> None:
        super().__init__()

    def columns(self) -> list:
        return [
            "songs.id", 
            "songs.title", 
            "songs.duration", 
            "songs.bitrate", 
            "songs.filesize", 
            "songs.release_year", 
            "songs.is_free", 
            "songs.filepath", 
            "songs.cover_image", 
            "artists.name as artist", 
            "albums.title as album", 
            "genres.name as genre"
        ]

    def process(self):

        return self.builder.table("songs") \
            .select(self.columns()) \
            .left_join("artists", "songs.artist_id", "=", "artists.id") \
            .left_join("albums", "songs.album_id", "=", "albums.id") \
            .left_join("genres", "songs.genre_id", "=", "genres.id") \
            .left_join("song_downloads", "songs.id", "=", "song_downloads.song_id") \
            .left_join("song_plays", "songs.id", "=", "song_plays.song_id") \
            .left_join("song_likes", "songs.id", "=", "song_likes.song_id") \
            .sum("song_downloads.download_count as downloads") \
            .sum("song_plays.play_count as plays") \
            .count("song_likes.id as likes") \
            .group_by("songs.id") \
            .when(self.filters, lambda query: query.where(self.filters) ) \
            .when(self.sort_by, lambda query: query.order_by(self.sort_by) ) \
            .paginate(self.per_page, self.page)
