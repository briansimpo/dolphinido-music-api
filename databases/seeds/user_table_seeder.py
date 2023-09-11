"""UserTableSeeder Seeder."""
from masoniteorm.seeds import Seeder
from masonite.facades import Hash

from app.models.User import User


class UserTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        User.create({
            'name': 'Artist', 
            'email': 'artist@example.com', 
            'password': Hash.make('password') 
        })

        User.create({
            'name': 'Fan', 
            'email': 'fan@example.com', 
            'password': Hash.make('password') 
        })

        User.create({
            'name': 'Admin', 
            'email': 'admin@example.com', 
            'password': Hash.make('password') 
        })

       
      
