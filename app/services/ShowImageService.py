from masoniteorm import Model
from app.config.uploads import SHOW_IMAGE_DIR
from app.services import FileUploadService
from app.models import Show


class ShowImageService(FileUploadService):

	def store(self, show: Show | Model, image_path):
		cover_image = self.upload(image_path, SHOW_IMAGE_DIR)
		show.cover_image = cover_image
		show.save()
		return show

	def update(self, show: Show | Model, image_path):
		new_image = self.upload(image_path, SHOW_IMAGE_DIR)
		old_image = show.cover_image
		show.cover_image = new_image
		show.save()
		self.delete(old_image)
		return show



