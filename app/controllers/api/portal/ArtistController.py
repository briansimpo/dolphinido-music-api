from masonite.controllers import Controller
from masonite.request import Request
from masonite.response import Response

from app.models import Artist, User
from app.repositories import ArtistRepository


class ArtistController(Controller):

	def __init__(self, artist_repository: ArtistRepository):
		self.artist_repository = artist_repository

	def index(self):
		pass

	def show(self, request: Request, response: Response):
		user = User.find(record_id=request.input("user_id"))
		artist = self.artist_repository.get_by_id(user.id)
		return response.json(artist.serialize())

	def store(self, request: Request, response: Response):
		user_id = request.input("user_id")
		user = User.find(record_id=user_id)

		if(user is None):
			return response.json({"message": "User not found"}, status=404)

		artist = Artist.create({
			"id": user_id,
			"name": request.input("name"),
			"birthday": request.input("birthday"),
			"country": request.input("country"),
			"city": request.input("city"),
			"artist_type_id": request.input("artist_type")
		})

		if artist is None:
			return response.json({"message": "Failed to create record"}, status=500)
		
		user.become_artist()
		
		return response.json(artist.serialize())

	def update(self, id, request: Request, response: Response):
		artist = self.artist_repository.get_by_id(id)
		artist.update({
			"name": request.input("name"),
			"birthday": request.input("birthday"),
			"country": request.input("country"),
			"city": request.input("city"),
			"artist_type_id": request.input("artist_type")
		})

		return response.json(artist.serialize())

	def destroy(self):
		pass
