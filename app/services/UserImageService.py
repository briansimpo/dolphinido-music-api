from masoniteorm import Model
from app.utils.helpers import get_url_path, get_rel_path
from app.config.uploads import USER_IMAGE_DIR
from app.services import FileUploadService
from app.models import User


class UserImageService(FileUploadService):

	def store(self, user: User | Model, image_path):
		image = self.upload(image_path, USER_IMAGE_DIR)
		user.image = image
		user.save()
		return user

	def update(self, user: User | Model, image_path):
		new_image = self.upload(image_path, USER_IMAGE_DIR)
		old_image = user.image
		user.image = new_image
		user.save()
		self.delete(old_image)
		return user



