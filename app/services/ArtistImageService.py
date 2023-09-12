from masoniteorm import Model

from app.config.uploads import ARTIST_IMAGE_DIR
from app.services import FileUploadService
from app.models import Artist


class ArtistImageService(FileUploadService):


	def store(self, artist: Artist | Model, image_path):
		image = self.upload(image_path, ARTIST_IMAGE_DIR)
		image_url = self.get_url_path(image)
		artist.image = image_url
		artist.save()
		return artist

	def update(self, artist: Artist | Model, image_path):
		new_image = self.upload(image_path, ARTIST_IMAGE_DIR)
		old_image = self.get_rel_path(artist.image)
		image_url = self.get_url_path(new_image)
		artist.image = image_url
		artist.save()
		self.delete(old_image)
		return artist



