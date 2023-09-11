from app.repositories.Repository import Repository


class PlaylistSongRepository(Repository):

	def get_songs(self, playlist_id):
		return self.query().with_meta()\
			.where("playlist_id", playlist_id)\
			.get()

	def get_song_count(self, playlist_id):
		return self.query()\
			.where("playlist_id", playlist_id)\
			.count()
