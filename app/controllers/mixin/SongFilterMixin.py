from masonite.request import Request
from app.controllers.mixin import PaginatorMixin
from app.filters import SongFilter

class SongFilterMixin(PaginatorMixin):
    
    def is_filterable(self, request: Request) -> bool:
        if request.input('genre') or request.input('sort'):
            return True
        else:
            return False
        
    def get_filters(self, request: Request) -> dict:
        genre = request.input("genre") or None
        filter = dict()
        if genre is not None:
            filter["genre_id"] = genre
        return filter
    
    def get_sorter(self, request: Request) -> str:
        sort_by = request.input("sort") or None
        return sort_by

    def filter(self, request: Request):
        
        filters = self.get_filters(request)
        sort_by = self.get_sorter(request)
        per_page = self.get_per_page(request)
        page = self.get_page(request)

        filter = SongFilter()
        filter.set_filters(filters)
        filter.set_sort(sort_by)
        filter.set_page(page)
        filter.set_per_page(per_page)

        songs = filter.process()

        return songs
    
    def filter_by_owner(self, request: Request):
        user = request.user()

        filters = self.get_filters(request)
        sort_by = self.get_sorter(request)
        per_page = self.get_per_page(request)
        page = self.get_page(request)

        filters["artist_id"]=user.id

        filter = SongFilter()
        filter.set_filters(filters)
        filter.set_sort(sort_by)
        filter.set_page(page)
        filter.set_per_page(per_page)

        songs = filter.process()

        return songs
    