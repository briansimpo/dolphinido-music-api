from .Repository import Repository
from .WorkFilterMixin import WorkFilterMixin


class ShowRepository(Repository, WorkFilterMixin):

    def get_by_artist(self, artist_id, limit: int = 20):
        return self.query().with_meta()\
            .where("artist_id", artist_id)\
            .paginate(limit)

    def count_by_artist(self, artist_id):
        return self.query().where("artist_id", artist_id).count()
