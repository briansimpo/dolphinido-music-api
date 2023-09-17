from tinytag import TinyTag
from pyaudioreader.audiofile import AudioFile
from app.config.uploads import (STORAGE_DIR, SONG_FILE_DIR)
from app.services import FileUploadService
from app.models import Song


class SongFileService(FileUploadService):

	def upload(self, uploaded_file, upload_dir=SONG_FILE_DIR):
		file_path = super().upload(uploaded_file, upload_dir)
		file_hash = AudioFile.get_hash(STORAGE_DIR + file_path)
		return file_path, file_hash

	def store(self, song: Song, song_file):
		filetag = TinyTag.get(STORAGE_DIR + song_file)
		song.file = song_file
		song.size = filetag.filesize
		song.duration = filetag.duration
		song.bitrate = filetag.bitrate
		song.save()
		return song