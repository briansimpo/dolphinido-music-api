from masoniteorm import Model
from app.config.uploads import SHOW_IMAGE_DIR
from app.services import FileUploadService
from app.models import Show
from app.utils.helpers import get_file_url


class ShowImageService(FileUploadService):

	def store(self, show: Show | Model, image_path):
		image_path = self.upload(SHOW_IMAGE_DIR, image_path)
		show.image_path = image_path
		show.image_url = get_file_url(image_path)
		show.save()
		return show

	def update(self, show: Show | Model, image_path):
		image_path = self.upload(SHOW_IMAGE_DIR, image_path)
		old_image = show.image_path
		show.image_path = image_path
		show.image_url = get_file_url(image_path)
		show.save()
		self.delete(old_image)
		return show



