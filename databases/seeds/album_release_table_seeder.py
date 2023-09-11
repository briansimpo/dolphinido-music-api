"""AlbumReleaseTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.models.AlbumRelease import AlbumRelease


class AlbumReleaseTableSeeder(Seeder):

    def run(self):
        """Run the database seeds."""
        AlbumRelease.create({
            'name': 'Single',
            'slug': 'single'
        })

        AlbumRelease.create({
            'name': 'Album',
            'slug': 'album'
        })

        AlbumRelease.create({
            'name': 'EP',
            'slug': 'ep'
        })

        AlbumRelease.create({
            'name': 'Mixtape',
            'slug': 'mixtape'
        })
