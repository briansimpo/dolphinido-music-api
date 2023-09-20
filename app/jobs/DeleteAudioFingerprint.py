import os
from masonite.queues import Queueable
from masonitedolphinido.dolphinido import Dolphinido
from app.models import Song


class DeleteAudioFingerprint(Queueable):

    def __init__(self, song: Song):
        self.song = song

    def handle(self):
        dolphinido = Dolphinido()
        audio = dolphinido.find_audio(self.song.id)
        audio.delete()


