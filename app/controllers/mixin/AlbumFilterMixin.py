from masonite.request import Request
from app.controllers.mixin import PaginatorMixin

class AlbumFilterMixin(PaginatorMixin):
    
    def is_filterable(self, request: Request) -> bool:
        if request.input('genre') \
        or request.input('is_free') \
        or request.input('is_published') \
        or request.input('sort'):
            return True
        else:
            return False
        
    def get_filters(self, request: Request) -> dict:
        genre = request.input("genre") or None
        is_free = request.input("is_free") or None
        is_published = request.input("is_published") or None
        filter = dict()
        if genre is not None:
            filter["genre_id"] = genre
        if is_free is not None:
            filter["is_free"] = bool(is_free)
        if is_published is not None:
            filter["is_published"] = bool(is_published)
        return filter
    
    def get_sorter(self, request: Request) -> str:
        sort_by = request.input("sort") or None
        return sort_by