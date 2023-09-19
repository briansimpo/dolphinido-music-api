import os
from tinytag import TinyTag
from pyaudioreader.audiofile import AudioFile
from app.config.uploads import SONG_FILE_DIR
from app.services import FileUploadService
from app.models import Song


class SongFileService(FileUploadService):

	def upload_file(self, uploaded_file):
		file_path = super().upload(SONG_FILE_DIR, uploaded_file)
		return file_path
	
	def get_file_hash(self, file_path):
		file_hash = AudioFile.get_hash(self.resolve(file_path))
		return file_hash

	def store(self, song: Song, file_path):
		filetag = TinyTag.get(self.resolve(file_path))
		song.filesize = filetag.filesize
		song.duration = filetag.duration
		song.bitrate = filetag.bitrate
		song.save()
		return song