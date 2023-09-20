from masoniteorm.models import Model
from masoniteorm.scopes import UUIDPrimaryKeyMixin
from masoniteorm.relationships import belongs_to, belongs_to_many
from app.builders import HasBuilder, ShowBuilder


class Show(Model, UUIDPrimaryKeyMixin, HasBuilder):
    __fillable__ = ['id', 'title', 'venue', 'description', 'country', 'city', 'contact_email', 'contact_number', 'ticket_price',
                    'event_date', 'event_time', 'is_free', 'is_public', 'is_published', 'cover_image', 'artist_id']

    __dates__ = ["event_date"]

    def publish(self):
        self.__setattr__('is_published', True)
        return self.save()

    def unpublish(self):
        self.__setattr__('is_published', False)
        return self.save()

    def make_public(self):
        self.__setattr__('is_public', True)
        return self.save()

    def make_private(self):
        self.__setattr__('is_public', False)
        return self.save()

    def get_builder(self):
        return self.new_builder(ShowBuilder)

    @belongs_to('artist_id', 'id')
    def artist(self):
        from app.models.Artist import Artist
        return Artist

    @belongs_to_many('show_id', 'artist_id', 'id', 'id', 'show_performers')
    def performers(self):
        from app.models.Artist import Artist
        return Artist
