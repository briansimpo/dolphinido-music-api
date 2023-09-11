from masonite.views import View
from masonite.controllers import Controller


class WelcomeController(Controller):

    def index(self, view: View):
        return view.render("welcome")

    

