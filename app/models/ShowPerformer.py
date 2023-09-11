from masoniteorm.models import Model
from masoniteorm.relationships import belongs_to
from app.builders import HasBuilder, ShowPerformerBuilder


class ShowPerformer(Model, HasBuilder):
    __fillable__ = ['id', 'show_id', 'artist_id']

    def get_builder(self):
        return self.new_builder(ShowPerformerBuilder)

    @belongs_to('show_id', 'id')
    def show(self):
        from app.models.Show import Show
        return Show
    
    @belongs_to('artist_id', 'id')
    def performer(self):
        from app.models.Artist import Artist
        return Artist

