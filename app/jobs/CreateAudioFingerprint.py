import os
from masonite.queues import Queueable
from masonitedolphinido.dolphinido import Dolphinido
from app.config.uploads import STORAGE_DIR
from app.models import Song


class CreateAudioFingerprint(Queueable):

    def __init__(self, song: Song):
        self.song = song

    def handle(self):
        dolphinido = Dolphinido()
        audio_id = self.song.id
        file_path = self.song.file_path
        audio_file = os.path.realpath(os.path.join(STORAGE_DIR, file_path))
        dolphinido.create_audio(audio_file, audio_id)


