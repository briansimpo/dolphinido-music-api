from masonite.controllers import Controller
from masonite.request import Request
from masonite.response import Response

from app.controllers.mixin import AlbumFilterMixin
from app.repositories import AlbumRepository, SongRepository
from app.services import AlbumImageService
from app.models import Album

class AlbumsController(Controller, AlbumFilterMixin):

    def __init__(self, album_repository: AlbumRepository, image_service: AlbumImageService, song_repository: SongRepository):
        self.album_repository = album_repository
        self.image_service = image_service
        self.song_repository = song_repository

    def getall(self, request: Request):
        user = request.user()
        albums = self.album_repository.get_by_artist(user.id)
        return albums
    
    def filter(self, request: Request):
        user = request.user()
        filters = self.get_filters(request)
        sort_by = self.get_sorter(request)
        per_page = self.get_per_page(request)
        page = self.get_page(request)
    
        filters["artist_id"]=user.id
        
        albums = self.album_repository.filter(filters, sort_by, per_page,page)
        return albums
    
    def index(self, request: Request, response: Response):
        try:
            if self.is_filterable(request) \
            or self.is_pageable(request):
                albums = self.filter(request)
            else:
                albums = self.getall(request)
            return response.json(albums.serialize())
        except:
            return response.json(self.empty())

    def show(self, id, response: Response):
        album = self.album_repository.get_by_id(id)
        album.track_count = album.total_tracks()
        album.duration = album.total_duration()
        album.tracks = self.song_repository.get_by_album(album_id=id)
        return response.json(album.serialize())

    def store(self, request: Request, response: Response):
        user = request.user()
        image = request.input("cover_image")

        album = Album.create({
            "artist_id": user.id,
            "title": request.input("title"),
            "year": request.input("year"),
            "genre_id": request.input("genre"),
            "album_release_id": request.input("album_release"),
        })

        self.image_service.store(album, image)

        return response.json(album.serialize(), 201)

    def update(self, id, request: Request, response: Response):
        album = self.album_repository.get_by_id(id)
        album.update({
            "title": request.input("title"),
            "year": request.input("year"),
            "genre_id": request.input("genre"),
            "album_release_id": request.input("album_release"),
        })
        return response.json(album.serialize())

    def destroy(self, id, response: Response):
        album = self.album_repository.get_by_id(id)
        old_image = album.cover_image
        album.delete()
        self.image_service.delete(old_image)

        return response.json(payload={"message": "album deleted"}, status=204)

    def publish(self, id, response: Response):
        album = self.album_repository.get_by_id(id)
        album.publish()
        return response.json(album.serialize())

    def unpublish(self, id, response: Response):
        album = self.album_repository.get_by_id(id)
        album.unpublish()
        return response.json(album.serialize())


