from masonite.authentication import Auth
from masonite.request import Request
from masonite.response import Response
from masonite.api.facades import Api
from masonite.facades import Hash
from masonite.controllers import Controller
from app.repositories import UserRepository
from app.models import User

class AuthController(Controller):

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
    
    def user(self, request: Request, response: Response):
        user = request.user()
        if user:
            return response.json({"data": user.serialize()})

        return response.json({"message": "Authentication token missing"}, status="401")
    
    def login(self, auth: Auth, request: Request, response: Response):
        user = auth.attempt(request.input("username"), request.input("password"))

        if user:
            user.generate_jwt()
            return response.json({"data": user.serialize()})

        return response.json({"message": "Username or Password is incorrect"}, status="403")
    
    def logout(self, request: Request, response: Response):
        user = request.user()
        if user:
            user.api_token = None
            user.save()
            return response.json({"message": "Signout successful"})

        return response.json({"message": "Signout failed"}, status="403")
    
    def register(self, request: Request, response: Response):
        name = request.input("name")
        email = request.input("email")
        password = Hash.make(request.input("password"))

        user_exists = self.user_repository.user_exists(email)

        if user_exists:
            return response.json({"message": "Username already exists"})

        user = User.create({
            "name": name,
            "email": email,
            "password": password
        })
        return response.json({"data": user.serialize()})
    
    def auth(self, auth: Auth, request: Request, response: Response):
        user = auth.attempt(request.input("username"), request.input("password"))

        if user:
            return response.json({"data": user.generate_jwt()})

        return response.json({"message": "Username or Password is incorrect"}, status="403")

    def reauth(self, request: Request, response: Response):
        user = Api.attempt_by_token(request.input("token"))

        if user:
            return response.json({"data": user.generate_jwt()})

        return response.json(
            {"message": "Could not reauthenticate based on given token."}, status="403"
        )

    

