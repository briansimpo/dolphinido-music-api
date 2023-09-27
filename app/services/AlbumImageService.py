from masoniteorm import Model
from app.config.uploads import ALBUM_IMAGE_DIR
from app.services import FileUploadService
from app.models import Album
from app.utils.helpers import get_file_url

class AlbumImageService(FileUploadService):

	def store(self, album: Album | Model, image_path):
		image_path = self.upload(ALBUM_IMAGE_DIR, image_path)
		album.image_path = image_path
		album.image_url = get_file_url(image_path)
		album.save()
		return album

	def update(self, album: Album | Model, image_path):
		image_path = self.upload(ALBUM_IMAGE_DIR, image_path)
		old_image = album.image_path
		album.image_path = image_path
		album.image_url = get_file_url(image_path)
		album.save()
		self.delete(old_image)
		return album



