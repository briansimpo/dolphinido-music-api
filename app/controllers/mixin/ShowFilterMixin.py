from masonite.request import Request
from app.controllers.mixin import AbstractFilterMixin

class ShowFilterMixin(AbstractFilterMixin):
    
    def is_filterable(self, request: Request) -> bool:
        if request.input('country') \
        or request.input('city') \
        or request.input('venue') \
        or request.input('is_free') \
        or request.input('is_published') \
        or request.input('sort'):
            return True
        else:
            return False
        
    def get_filters(self, request: Request) -> dict:
        country = request.input("country") or None
        city = request.input("city") or None
        venue = request.input("venue") or None
        is_free = request.input("is_free") or None
        is_published = request.input("is_published") or None
        filter = dict()
        if country is not None:
            filter["country"] = country
        if country is not None:
            filter["city"] = city
        if country is not None:
            filter["venue"] = venue
        if is_free is not None:
            filter["is_free"] = bool(is_free)
        if is_published is not None:
            filter["is_published"] = bool(is_published)
        return filter