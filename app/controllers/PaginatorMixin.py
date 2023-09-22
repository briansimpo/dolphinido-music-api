from masonite.request import Request

class PaginatorMixin:

	def paginator(self, request: Request):
		per_page = request.input('limit') or 20
		page = request.input('page') or 1
		return int(per_page), int(page)



