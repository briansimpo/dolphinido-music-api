from masoniteorm.models import Model
from masoniteorm.relationships import belongs_to
from app.builders import HasBuilder, FollowingBuilder


class Following(Model, HasBuilder):
    __fillable__ = ['id', 'user_id', 'artist_id']

    def get_builder(self):
        return self.new_builder(FollowingBuilder)

    @belongs_to('user_id', 'id')
    def user(self):
        from app.models.User import User
        return User

    @belongs_to('artist_id', 'id')
    def artist(self):
        from app.models.Artist import Artist
        return Artist
