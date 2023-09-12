from masoniteorm import Model

from app.config.uploads import USER_IMAGE_DIR
from app.services import FileUploadService
from app.models import User


class UserImageService(FileUploadService):

	def store(self, user: User | Model, image_path):
		image = self.upload(image_path, USER_IMAGE_DIR)
		image_url = self.get_url_path(image)
		user.image = image_url
		user.save()
		return user

	def update(self, user: User | Model, image_path):
		new_image = self.upload(image_path, USER_IMAGE_DIR)
		old_image = self.get_rel_path(user.image)
		image_url = self.get_url_path(new_image)
		user.image = image_url
		user.save()
		self.delete(old_image)
		return user



