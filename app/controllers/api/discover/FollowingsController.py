from masonite.controllers import Controller
from masonite.request import Request
from masonite.response import Response

from app.models import Following
from app.repositories import ArtistRepository, FollowingRepository


class FollowingsController(Controller):

    def __init__(self, artist_repository: ArtistRepository, following_repository: FollowingRepository):
        self.artist_repository = artist_repository
        self.following_repository = following_repository

    def index(self, response: Response):
        followings = self.following_repository.get_all()
        return response.json(followings.serialize())

    def show(self, id, response: Response):
        following = self.following_repository.get_by_id(id)
        return response.json(following.serialize())

    def store(self, id, request: Request, response: Response):
        user = request.user()
        artist = self.artist_repository.get_by_id(id)

        following_exists = self.following_repository.following_exists(user.id, artist.id)

        if not following_exists:
            Following.create({
                "user_id": user.id,
                "artist_id": artist.id
            })

        return response.json(artist.serialize())

    def destroy(self, id, response: Response):
        following = self.following_repository.get_by_id(id)
        following.delete()
        return response.json(payload={"message": "artist unfollowed"}, status=204)
