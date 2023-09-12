import os
from masonite.queues import Queueable
from masonitedolphinido.dolphinido import Dolphinido
from app.utils.helpers import get_rel_path
from app.config.uploads import STORAGE_DIR
from app.models import Song


class Fingerprint(Queueable):

    def __init__(self, song_id):
        self.song_id = song_id

    def handle(self):

        dolphinido = Dolphinido()

        song = Song.find(self.song_id)

        audio_id = song.id
        file_path = get_rel_path(song.file)
        audio_file = os.path.realpath(STORAGE_DIR + file_path)
        
        dolphinido.create_audio(audio_file, audio_id)

