from tinytag import TinyTag
from slugify import slugify
from pyaudioreader.audiofile import AudioFile
from app.config.uploads import SONG_FILE_DIR
from app.services import FileUploadService
from app.models import Song, Genre


class SongFileService(FileUploadService):

	def upload_file(self, uploaded_file):
		file_path = super().upload(SONG_FILE_DIR, uploaded_file)
		return file_path
	
	def get_file_hash(self, file_path):
		resolved_path = self.resolve(file_path)
		file_hash = AudioFile.get_hash(resolved_path)
		return file_hash	

	def store(self, song: Song, file_path):
		resolved_path = self.resolve(file_path)
		filetag = TinyTag.get(resolved_path)
		genre = self.get_genre(filetag.genre)

		song.filesize = filetag.filesize
		song.duration = filetag.duration
		song.bitrate = filetag.bitrate
		song.release_year = filetag.year
		if genre:
			song.genre_id = genre.id
		song.save()
		return song
	
	def get_genre(self, name):
		try:
			slug = slugify(name)
			genre = Genre.first_or_create(
				wheres={'slug': slug}, 
				creates={'name': name, 'slug': slug}
			)
			return genre
		except Exception as e:
			print(e)

