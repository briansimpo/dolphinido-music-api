from masoniteorm import Model
from app.config.uploads import ALBUM_IMAGE_DIR
from app.services import FileUploadService
from app.models import Album


class AlbumImageService(FileUploadService):

	def store(self, album: Album | Model, image_path):
		cover_image = self.upload(ALBUM_IMAGE_DIR, image_path)
		album.cover_image = cover_image
		album.save()
		return album

	def update(self, album: Album | Model, image_path):
		new_image = self.upload(ALBUM_IMAGE_DIR, image_path)
		old_image = album.cover_image
		album.cover_image = new_image
		album.save()
		self.delete(old_image)
		return album



