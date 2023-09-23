import os
import shutil
import uuid
from masonite.filesystem import Storage
from app.config.uploads import STORAGE_DISK, STORAGE_DIR, PLACEHOLDER

class FileUploadService:

	def __init__(self, storage: Storage):
		self.storage = storage

	def upload(self, upload_dir, uploaded_file):
		return self.storage.disk(STORAGE_DISK).put_file(upload_dir, uploaded_file)

	def delete(self, file_path):
		try:
			resolved_path = self.resolve(file_path)
			os.remove(resolved_path)
		except OSError as e:
			print(e)
	
	def resolve(self, file_path: str):
		return os.path.join(STORAGE_DIR, file_path)

	def placeholder(self, destination_dir):
		extension = ".png"
		placeholder_file = self.__placeholder()

		random_file = self.__random_name() + extension
		upload_file = os.path.join(destination_dir, random_file)
		destination_file = self.resolve(upload_file)
		try:
			path = shutil.copy(placeholder_file, destination_file)
			return path
		except Exception as e:
			print(e)

	def __placeholder(self):
		return self.resolve(PLACEHOLDER)
	
	def __random_name(self):
		return uuid.uuid4()
