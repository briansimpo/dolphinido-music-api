from tinytag import TinyTag
from app.config.uploads import (STORAGE_DIR, SONG_FILE_DIR)
from app.services import FileUploadService
from app.models import Song


class SongFileService(FileUploadService):


	def upload(self, uploaded_file, upload_dir=SONG_FILE_DIR):
		file_path = super().upload(uploaded_file, upload_dir)
		return file_path

	def store(self, song: Song, song_file):
		filemeta = TinyTag.get(STORAGE_DIR + song_file)
		song.file = song_file
		song.size = filemeta.filesize
		song.duration = filemeta.duration
		song.bitrate = filemeta.bitrate
		song.save()
		return song
