from masonite.controllers import Controller
from masonite.request import Request
from masonite.response import Response

from app.controllers.PaginatorMixin import PaginatorMixin
from app.models import Show
from app.repositories import ShowRepository
from app.services import ShowImageService


class ShowsController(Controller, PaginatorMixin):

    def __init__(self, show_repository: ShowRepository, image_service: ShowImageService):
        self.show_repository = show_repository
        self.image_service = image_service

    def index(self, request: Request, response: Response):
        user = request.user()
        per_page, page = self.paginator(request)
        shows = self.show_repository.get_by_artist(user.id, per_page, page)
        return response.json(shows.serialize())

    def show(self, id, response: Response):
        show = self.show_repository.get_by_id(id)
        return response.json(show.serialize())

    def store(self, request: Request, response: Response):
        user = request.user()
        uploaded_image = request.input("cover_image")

        show = Show.create({
            "artist_id": user.id,
            "title": request.input("title"),
            "description": request.input("description"),
            "country": request.input("country"),
            "venue": request.input("venue"),
            "seats": request.input("seats"),
            "city": request.input("city"),
            "is_free": request.input("is_free"),
            "ticket_price": request.input("ticket_price"),
            "contact_email": request.input("contact_email"),
            "contact_number": request.input("contact_number"),
            "event_date": request.input("event_date"),
            "event_time": request.input("event_time"),
        })

        self.image_service.store(show, uploaded_image)

        return response.json(show.serialize(), 201)

    def update(self, id, request: Request, response: Response):

        show = self.show_repository.get_by_id(id)

        show.update({
            "title": request.input("title"),
            "description": request.input("description"),
            "country": request.input("country"),
            "venue": request.input("venue"),
            "seats": request.input("seats"),
            "city": request.input("city"),
            "is_free": request.input("is_free"),
            "ticket_price": request.input("ticket_price"),
            "contact_email": request.input("contact_email"),
            "contact_number": request.input("contact_number"),
            "event_date": request.input("event_date"),
            "event_time": request.input("event_time"),
        })
        return response.json(show.serialize())

    def destroy(self, id, response: Response):
        show = self.show_repository.get_by_id(id)
        old_image = show.cover_image
        show.delete()
        self.image_service.delete(old_image)
        return response.json(payload={"message": "show deleted"}, status=204)

    def publish(self, id, response: Response):
        show = self.show_repository.get_by_id(id)
        show.publish()
        return response.json(show.serialize())

    def unpublish(self, id, response: Response):
        show = self.show_repository.get_by_id(id)
        show.unpublish()
        return response.json(show.serialize())



