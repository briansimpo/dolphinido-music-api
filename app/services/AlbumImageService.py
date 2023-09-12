from masoniteorm import Model

from app.config.uploads import ALBUM_IMAGE_DIR
from app.services import FileUploadService
from app.models import Album


class AlbumImageService(FileUploadService):

	def store(self, album: Album | Model, image_path):
		cover_image = self.upload(image_path, ALBUM_IMAGE_DIR)
		image_url = self.get_url_path(cover_image)
		album.cover_image = image_url
		album.save()
		return album

	def update(self, album: Album | Model, image_path):
		new_image = self.upload(image_path, ALBUM_IMAGE_DIR)
		old_image = self.get_rel_path(album.cover_image)
		image_url = self.get_url_path(new_image)
		album.cover_image = image_url
		album.save()
		self.delete(old_image)
		return album



