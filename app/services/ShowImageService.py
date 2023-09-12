from masoniteorm import Model

from app.config.uploads import SHOW_IMAGE_DIR
from app.services import FileUploadService
from app.models import Show


class ShowImageService(FileUploadService):

	def store(self, show: Show | Model, image_path):
		cover_image = self.upload(image_path, SHOW_IMAGE_DIR)
		image_url = self.get_url_path(cover_image)
		show.cover_image = image_url
		show.save()
		return show

	def update(self, show: Show | Model, image_path):
		new_image = self.upload(image_path, SHOW_IMAGE_DIR)
		old_image = self.get_rel_path(show.cover_image)
		image_url = self.get_url_path(new_image)
		show.cover_image = image_url
		show.save()
		self.delete(old_image)
		return show



