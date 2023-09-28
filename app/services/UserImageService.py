from masoniteorm import Model
from app.config.uploads import USER_IMAGE_DIR
from app.services import FileUploadService
from app.models import User
from app.utils.helpers import get_file_url


class UserImageService(FileUploadService):

	def store(self, user: User | Model, image_path):
		image_path = self.upload(USER_IMAGE_DIR, image_path)
		user.image_path = image_path
		user.image_url = get_file_url(image_path)
		user.save()
		return user

	def update(self, user: User | Model, image_path):
		image_path = self.upload(USER_IMAGE_DIR, image_path)
		old_image = user.image_path
		user.image_path = image_path
		user.image_url = get_file_url(image_path)
		user.save()
		self.delete(old_image)
		return user



