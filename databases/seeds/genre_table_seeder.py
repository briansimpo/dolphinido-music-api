"""GenreTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.models.Genre import Genre


class GenreTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        Genre.create({
            'name': 'Afro', 
            'slug': 'afro'
        })

        Genre.create({
            'name': 'Afro pop', 
            'slug': 'afro_pop'
        })

        Genre.create({
            'name': 'Afro beat', 
            'slug': 'afro_beat'
        })

        Genre.create({
            'name': 'Amapiano', 
            'slug': 'amapiano'
        })

        Genre.create({
            'name': 'Blues', 
            'slug': 'blues'
        })

        Genre.create({
            'name': 'Calypso', 
            'slug': 'calypso'
        })

        Genre.create({
            'name': 'Classical', 
            'slug': 'classical'
        })

        Genre.create({
            'name': 'Country', 
            'slug': 'country'
        })

        Genre.create({
            'name': 'Dancehall', 
            'slug': 'dancehall'
        })

        Genre.create({
            'name': 'Electronic Dance', 
            'slug': 'electronic_dance'
        })

        Genre.create({
            'name': 'Funk', 
            'slug': 'funk'
        })

        Genre.create({
            'name': 'Gospel', 
            'slug': 'gospel'
        })

        Genre.create({
            'name': 'Gospel Hip Hop', 
            'slug': 'gospel_hip_hop'
        })

        Genre.create({
            'name': 'House', 
            'slug': 'house'
        })

        Genre.create({
            'name': 'Hip Hop', 
            'slug': 'hip_hop'
        })

        Genre.create({
            'name': 'Jazz', 
            'slug': 'jazz'
        })

        Genre.create({
            'name': 'Kwaito', 
            'slug': 'kwaito'
        })

        Genre.create({
            'name': 'Kwasakwasa', 
            'slug': 'kwasakwasa'
        })

        Genre.create({
            'name': 'Lokolo', 
            'slug': 'lokolo'
        })

        Genre.create({
            'name': 'Malimba', 
            'slug': 'malimba'
        })

        Genre.create({
            'name': 'Ndombolo', 
            'slug': 'ndombolo'
        })

        Genre.create({
            'name': 'Pop', 
            'slug': 'pop'
        })

        Genre.create({
            'name': 'Rap', 
            'slug': 'rap'
        })

        Genre.create({
            'name': 'RnB', 
            'slug': 'r_n_b'
        })

        Genre.create({
            'name': 'Reggae', 
            'slug': 'reggae'
        })

        Genre.create({
            'name': 'Rock', 
            'slug': 'rock'
        })

        Genre.create({
            'name': 'Rumba', 
            'slug': 'rumba'
        })

        Genre.create({
            'name': 'Trap', 
            'slug': 'trap'
        })

        Genre.create({
            'name': 'Techno', 
            'slug': 'techno'
        })

        Genre.create({
            'name': 'Soul', 
            'slug': 'soul'
        })

        Genre.create({
            'name': 'Urban', 
            'slug': 'urban'
        })

        Genre.create({
            'name': 'Unknown', 
            'slug': 'unknown'
        })

        Genre.create({
            'name': 'Zamakolo', 
            'slug': 'zamakolo'
        })
