from masoniteorm import Model
from app.config.uploads import SONG_IMAGE_DIR
from app.services import FileUploadService
from app.models import Song
from app.utils.helpers import get_file_url


class SongImageService(FileUploadService):

	def store(self, song: Song | Model, image_path):
		image_path = self.upload(SONG_IMAGE_DIR, image_path)
		song.image_path = image_path
		song.image_url = get_file_url(image_path)
		song.save()
		return song

	def update(self, song: Song | Model, image_path):
		image_path = self.upload(SONG_IMAGE_DIR, image_path)
		old_image = song.image_path
		song.image_path = image_path
		song.image_url = get_file_url(image_path)
		song.save()
		self.delete(old_image)
		return song

	def default(self, song: Song):
		image_path = self.placeholder(SONG_IMAGE_DIR)
		song.image_path = image_path
		song.image_url = get_file_url(image_path)
		song.save()
		return song


		



