from masonite.request import Request

class PaginatorMixin:
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
	