"""Base Database Seeder Module."""
from masoniteorm.seeds import Seeder

from .user_table_seeder import UserTableSeeder
from .album_release_table_seeder import AlbumReleaseTableSeeder
from .artist_type_table_seeder import ArtistTypeTableSeeder
from .genre_table_seeder import GenreTableSeeder


class DatabaseSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        self.call(
            UserTableSeeder,
            AlbumReleaseTableSeeder,
            ArtistTypeTableSeeder,
            GenreTableSeeder,
        )
        
