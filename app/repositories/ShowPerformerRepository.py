from app.repositories.Repository import Repository


class ShowPerformerRepository(Repository):

	def get_performers(self, show_id):
		return self.query().with_meta()\
			.where("show_id", show_id)\
			.get()

	def get_performer_count(self, show_id):
		return self.query()\
			.where("show_id", show_id)\
			.count()

	def performer_exists(self, artist_id, show_id):
		return self.query() \
			.where("show_id", show_id) \
			.where("artist_id", artist_id) \
			.exists()
