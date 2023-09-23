from masoniteorm import Model
from app.config.uploads import ARTIST_IMAGE_DIR
from app.services import FileUploadService
from app.models import Artist


class ArtistImageService(FileUploadService):

	def store(self, artist: Artist | Model, image_path):
		image = self.upload(ARTIST_IMAGE_DIR, image_path)
		artist.image = image
		artist.save()
		return artist

	def update(self, artist: Artist | Model, image_path):
		new_image = self.upload(ARTIST_IMAGE_DIR, image_path)
		old_image = artist.image
		artist.image = new_image
		artist.save()
		self.delete(old_image)
		return artist



