from masoniteorm import Model
from app.config.uploads import ARTIST_IMAGE_DIR
from app.services import FileUploadService
from app.models import Artist
from app.utils.helpers import get_file_url


class ArtistImageService(FileUploadService):

	def store(self, artist: Artist | Model, image_path):
		image_path = self.upload(ARTIST_IMAGE_DIR, image_path)
		artist.image_path = image_path
		artist.image_url = get_file_url(image_path)
		artist.save()
		return artist

	def update(self, artist: Artist | Model, image_path):
		image_path = self.upload(ARTIST_IMAGE_DIR, image_path)
		old_image = artist.image_path
		artist.image_path = image_path
		artist.image_url = get_file_url(image_path)
		artist.save()
		self.delete(old_image)
		return artist



