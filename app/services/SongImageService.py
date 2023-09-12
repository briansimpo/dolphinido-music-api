from masoniteorm import Model
from app.utils.helpers import get_url_path, get_rel_path
from app.config.uploads import SONG_IMAGE_DIR
from app.services import FileUploadService
from app.models import Song


class SongImageService(FileUploadService):

	def store(self, song: Song | Model, image_path):
		cover_image = self.upload(image_path, SONG_IMAGE_DIR)
		image_url = get_url_path(cover_image)
		song.cover_image = image_url
		song.save()
		return song

	def update(self, song: Song | Model, image_path):
		new_image = self.upload(image_path, SONG_IMAGE_DIR)
		old_image = get_rel_path(song.cover_image)
		image_url = get_url_path(new_image)
		song.cover_image = image_url
		song.save()
		self.delete(old_image)
		return song



