from abc import ABC, abstractmethod
from masonite.request import Request

class AbstractFilterMixin(ABC):
	PER_PAGE = 100
	CURRENT_PAGE = 1

	def is_pageable(self, request: Request) -> bool:
		if request.input('page') or request.input('limit'):
			return True
		else:
			return False

	def get_per_page(self, request: Request) -> int :
		per_page = request.input('limit') or self.PER_PAGE
		return int(per_page)
	
	def get_page(self, request: Request) -> int:
		page = request.input('page') or self.CURRENT_PAGE
		return int(page)
	
	def get_sorter(self, request: Request) -> str:
		sort_by = request.input("sort") or None
		return sort_by
	
	def empty(self):
		data = {"data": [], "meta": {"last_page": 1 } }
		return data
	
	@abstractmethod
	def is_filterable(self, *kwargs) -> bool:
		pass
	
	@abstractmethod
	def get_filters(self, *kwargs) -> dict:
		pass
