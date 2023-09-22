class WorkFilterMixin:

	def get_published_recently(self, per_page=20, page=1):
		return self.query().with_meta()\
			.where("is_published", True) \
			.latest()\
			.paginate(per_page, page)

	def get_published_by_artist_recently(self, artist_id, per_page=20, page=1):
		return self.query().with_meta()\
			.where("is_published", True) \
			.where("artist_id", artist_id) \
			.latest()\
			.paginate(per_page, page)

	def get_added_by_artist_recently(self, artist_id, per_page=20, page=1):
		return self.query().with_meta()\
			.where("artist_id", artist_id) \
			.latest()\
			.paginate(per_page, page)

	def get_published(self, per_page=20, page=1):
		return self.query().with_meta()\
			.where("is_published", True) \
			.paginate(per_page, page)

	def count_published(self):
		return self.query()\
			.where("is_published", True)\
			.count()

	def get_published_by_artist(self, artist_id, per_page=20, page=1):
		return self.query().with_meta()\
			.where("is_published", True) \
			.where("artist_id", artist_id) \
			.paginate(per_page, page)

	def get_unpublished_by_artist(self, artist_id, per_page=20, page=1):
		return self.query().with_meta()\
			.where("is_published", False) \
			.where("artist_id", artist_id) \
			.paginate(per_page, page)

	def get_for_free(self, per_page=20, page=1):
		return self.query().with_meta()\
			.where("is_published", True) \
			.where("is_free", True) \
			.paginate(per_page, page)

	def count_for_free(self):
		return self.query().with_meta()\
			.where("is_published", True) \
			.where("is_free", True) \
			.count()

	def count_for_sale(self):
		return self.query()\
			.where("is_published", True) \
			.where("is_free", False) \
			.count()

	def get_for_sale(self, per_page=20, page=1):
		return self.query().with_meta()\
			.where("is_published", True) \
			.where("is_free", False) \
			.paginate(per_page, page)

	def get_for_free_by_genre(self, genre_id, per_page=20, page=1):
		return self.query().with_meta()\
			.where("genre_id", genre_id) \
			.where("is_free", True) \
			.paginate(per_page, page)

	def get_for_sale_by_genre(self, genre_id, per_page=20, page=1):
		return self.query().with_meta()\
			.where("genre_id", genre_id) \
			.where("is_free", False) \
			.paginate(per_page, page)

	def get_for_free_randomly(self, per_page=20, page=1):
		return self.query().with_meta()\
			.where("is_published", True) \
			.where("is_free", True) \
			.in_random_order() \
			.paginate(per_page, page)

	def get_for_free_by_genre_randomly(self, genre_id, per_page=20, page=1):
		return self.query().with_meta()\
			.where("genre_id", genre_id) \
			.where("is_free", True) \
			.in_random_order() \
			.paginate(per_page, page)



