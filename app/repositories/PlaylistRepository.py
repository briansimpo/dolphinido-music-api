from app.repositories.Repository import Repository


class PlaylistRepository(Repository):

	def get_playlists(self, user_id):
		return self.query().where("user_id", user_id).get()

	def get_playlist_count(self, user_id):
		return self.query().where("user_id", user_id).count()
