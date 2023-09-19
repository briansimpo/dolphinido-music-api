import os
from masonite.filesystem import Storage
from app.config.uploads import STORAGE_DISK, STORAGE_DIR


class FileUploadService:

	def __init__(self, storage: Storage):
		self.storage = storage

	def upload(self, upload_dir, uploaded_file):
		return self.storage.disk(STORAGE_DISK).put_file(upload_dir, uploaded_file)

	def resolve(file_path: str):
		return os.path.join(STORAGE_DIR, file_path)

	def delete(self, file_path):
		try:
			file = self.resolve(file_path)
			os.remove(file)
		except OSError as e:
			print(e)
	