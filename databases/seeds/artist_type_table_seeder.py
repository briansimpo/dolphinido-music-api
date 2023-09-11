"""ArtistTypeTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.models.ArtistType import ArtistType


class ArtistTypeTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        ArtistType.create({
            'name': 'Solo Artist',
            'slug': 'solo_artist'
        })

        ArtistType.create({
            'name': 'Band/Choir/Crew',
            'slug': 'band_choir_crew'
        })

        ArtistType.create({
            'name': 'Compound Artists',
            'slug': 'compound_artists'
        })
