from masonite.middleware import Middleware
from masonite.api.facades import Api


class ApiUserMiddleware(Middleware):
    """Middleware to check if the user is logged in."""

    def before(self, request, response):
        token = Api.get_token()
        if token:
            model = Api.attempt_by_token(token)
            request.set_user(user=model)
        return request

    def after(self, request, response):
        return request

