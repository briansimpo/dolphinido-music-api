import os
import shutil
from masonite.filesystem import Storage
from app.config.uploads import STORAGE_DISK
from app.services import FilePathResover


class FileUploadService:

	def __init__(self, storage: Storage, fileresolver: FilePathResover):
		self.storage = storage
		self.fileresolver = fileresolver

	def upload(self, upload_dir, uploaded_file):
		return self.storage.disk(STORAGE_DISK).put_file(upload_dir, uploaded_file)

	def delete(self, file_path):
		try:
			resolved_path = self.fileresolver.resolve(file_path)
			os.remove(resolved_path)
		except OSError as e:
			print(e)
	
	def placeholder(self, destination_dir):
		extension = ".png"
		placeholder_file = self.fileresolver.placeholder()

		random_file = self.fileresolver.random_name() + extension
		upload_file = os.path.join(destination_dir, random_file)
		destination_file = self.fileresolver.resolve(upload_file)
		try:
			path = shutil.copy(placeholder_file, destination_file)
			return path
		except Exception as e:
			print(e)