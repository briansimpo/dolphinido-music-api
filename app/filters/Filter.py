from masoniteorm.query import QueryBuilder
from abc import ABC, abstractmethod

class Filter(ABC):

    def __init__(self) -> None:
        super().__init__()
        self.builder = QueryBuilder()
        self.filters = dict
        self.sort_by = None
        self.per_page = 100
        self.page = 1

    def set_filters(self, filters: dict):
        self.filters = filters

    def set_sort(self, sort_by: str):
        self.sort_by = sort_by

    def set_page(self, page: int):
        self.page = page

    def set_per_page(self, per_page: int):
        self.per_page = per_page

    @abstractmethod
    def process(self):
        pass