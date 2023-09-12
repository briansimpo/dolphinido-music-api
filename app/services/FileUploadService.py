import os
from urllib.parse import urlparse
from masonite.environment import env
from masonite.filesystem import Storage
from app.config.uploads import STORAGE_DISK, STORAGE_DIR


class FileUploadService:

	def __init__(self, storage: Storage):
		self.storage = storage

	def upload(self, uploaded_file, upload_dir=STORAGE_DIR):
		return self.storage.disk(STORAGE_DISK).put_file(upload_dir, uploaded_file)

	def delete(self, file_path):
		try:
			os.remove(STORAGE_DIR + file_path)
		except OSError as e:
			print(e)
	
	def get_url_path(self, file_path):
		app_url = env("APP_URL")
		return app_url + "/" + file_path
	
	def get_rel_path(self, url):
		parsed_url = urlparse(url)
		return parsed_url.path
