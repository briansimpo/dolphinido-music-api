class WorkFilterMixin:

	def get_published_recently(self, limit: int = 20):
		return self.query().with_meta()\
			.where("is_published", True) \
			.latest()\
			.limit(limit)\
			.get()

	def get_published_by_artist_recently(self, artist_id, limit: int = 20):
		return self.query().with_meta()\
			.where("is_published", True) \
			.where("artist_id", artist_id) \
			.latest()\
			.limit(limit)\
			.get()

	def get_added_by_artist_recently(self, artist_id, limit: int = 20):
		return self.query().with_meta()\
			.where("artist_id", artist_id) \
			.latest()\
			.limit(limit)\
			.get()

	def get_published(self, limit: int = 20):
		return self.query().with_meta()\
			.where("is_published", True) \
			.paginate(limit)

	def count_published(self):
		return self.query()\
			.where("is_published", True)\
			.count()

	def get_published_by_artist(self, artist_id, limit: int = 20):
		return self.query().with_meta()\
			.where("is_published", True) \
			.where("artist_id", artist_id) \
			.paginate(limit)

	def get_unpublished_by_artist(self, artist_id, limit: int = 20):
		return self.query().with_meta()\
			.where("is_published", False) \
			.where("artist_id", artist_id) \
			.paginate(limit)

	def get_for_free(self, limit: int = 20):
		return self.query().with_meta()\
			.where("is_published", True) \
			.where("is_free", True) \
			.paginate(limit)

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

	def get_for_sale(self, limit: int = 20):
		return self.query().with_meta()\
			.where("is_published", True) \
			.where("is_free", False) \
			.paginate(limit)

	def get_for_free_by_genre(self, genre_id, limit: int = 20):
		return self.query().with_meta()\
			.where("genre_id", genre_id) \
			.where("is_free", True) \
			.paginate(limit)

	def get_for_sale_by_genre(self, genre_id, limit: int = 20):
		return self.query().with_meta()\
			.where("genre_id", genre_id) \
			.where("is_free", False) \
			.paginate(limit)

	def get_for_free_randomly(self, limit: int = 20):
		return self.query().with_meta()\
			.where("is_published", True) \
			.where("is_free", True) \
			.in_random_order() \
			.limit(limit)\
			.get()

	def get_for_free_by_genre_randomly(self, genre_id, limit: int = 20):
		return self.query().with_meta()\
			.where("genre_id", genre_id) \
			.where("is_free", True) \
			.in_random_order() \
			.limit(limit)\
			.get()



