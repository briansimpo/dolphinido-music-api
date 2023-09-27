
from app.filters import Filter


class AlbumFilter(Filter):
    
    def __init__(self) -> None:
        super().__init__()

    def columns(self) -> list:
        return [
            "albums.id", 
            "albums.title",
            "albums.year", 
            "albums.price", 
            "albums.is_free", 
            "albums.is_published", 
            "albums.image_url", 
            "artists.name as artist",  
            "genres.name as genre",
            "album_releases.name as album_release"
        ]

    def process(self):

        return self.builder.table("albums") \
            .select(self.columns()) \
            .left_join("artists", "albums.artist_id", "=", "artists.id") \
            .left_join("genres", "albums.genre_id", "=", "genres.id") \
            .left_join("album_releases", "albums.album_release_id", "=", "album_releases.id") \
            .left_join("album_downloads", "albums.id", "=", "album_downloads.album_id") \
            .left_join("album_likes", "albums.id", "=", "album_likes.album_id") \
            .sum("album_downloads.download_count as downloads") \
            .count("album_likes.id as likes") \
            .group_by("albums.id") \
            .when(self.filters, lambda query: query.where(self.filters) ) \
            .when(self.sort_by, lambda query: query.order_by(self.sort_by) ) \
            .paginate(self.per_page, self.page)
