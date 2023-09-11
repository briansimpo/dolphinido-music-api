from masonite.controllers import Controller
from masonite.request import Request
from masonite.response import Response

from app.models import Playlist
from app.repositories import PlaylistRepository, PlaylistSongRepository


class PlaylistsController(Controller):

    def __init__(self, playlist_repository: PlaylistRepository, playlist_songs: PlaylistSongRepository):
        self.playlist_repository = playlist_repository
        self.playlist_songs = playlist_songs

    def index(self, request: Request, response: Response):
        user = request.user()
        playlists = self.playlist_repository.get_playlists(user.id)
        return response.json(playlists.serialize())

    def show(self, id, response: Response):
        playlist = self.playlist_repository.get_by_id(id)
        playlist.playlist_songs = playlist.songs()
        return response.json(playlist.serialize())

    def store(self, request: Request, response: Response):
        user = request.user()
        name = request.input("name")
        playlist = Playlist.create({
            "user_id": user.id,
            "name": name
        })

        return response.json(playlist.serialize())

    def update(self, id, request: Request, response: Response):
        playlist = self.playlist_repository.get_by_id(id)
        name = request.input("name")
        playlist.update({
            "name": name
        })
        return response.json(playlist.serialize())

    def destroy(self, id, response: Response):
        playlist = self.playlist_repository.get_by_id(id)
        playlist.delete()
        return response.json(payload={"message": "playlist deleted"}, status=204)
