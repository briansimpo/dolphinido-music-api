import os
import shutil
import uuid
import pathlib
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
		placeholder = self.__placeholder()
		extension = self.__extension(placeholder)
		random_name = self.__random_name()

		try:
			resolve_dir = self.resolve(destination_dir)
			os.mkdir(resolve_dir)
		except:
			pass	

		try:
			random_file = "{}{}".format(random_name, extension)
			upload_file = os.path.join(destination_dir, random_file)
			copy_file = self.resolve(upload_file)
			path = shutil.copy(placeholder, copy_file)
			if os.path.exists(path):
				return upload_file
		except:
			pass
	
	def __placeholder(self):
		return self.resolve(PLACEHOLDER)
	
	def __random_name(self):
		return uuid.uuid4()

	def __extension(self, file_path):
		return os.path.splitext(os.path.basename(file_path))[1]