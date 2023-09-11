from masonite.api import Api
from masonite.routes import Route

ROUTES = [
	# Index page 
	Route.get("/", "WelcomeController@index"),

    # Register user and return user object
    Route.post("/api/register", "auth.AuthController@register"),

    # Login user and return user object
    Route.post("/api/login", "auth.AuthController@login"),

    # Logout user and delete user token
    Route.post("/api/logout", "auth.AuthController@logout"),

    # Login user and return JWT token
    Route.post("/api/auth", "auth.AuthController@auth"),

    # Refresh JWT token
    Route.post("/api/reauth", "auth.AuthController@reauth"),
   
]

