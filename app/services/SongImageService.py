from masoniteorm import Model
from app.config.uploads import SONG_IMAGE_DIR
from app.services import FileUploadService
from app.models import Song


class SongImageService(FileUploadService):

	def store(self, song: Song | Model, image_path=None):
		cover_image = None
		if image_path is None:
			cover_image = self.placeholder(SONG_IMAGE_DIR)
		else:
			cover_image = self.upload(SONG_IMAGE_DIR, image_path)
		song.cover_image = cover_image
		song.save()
		return song

	def update(self, song: Song | Model, image_path):
		new_image = self.upload(SONG_IMAGE_DIR, image_path)
		old_image = song.cover_image
		song.cover_image = new_image
		song.save()
		self.delete(old_image)
		return song

		



