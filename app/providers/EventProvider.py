from masonite.providers import Provider


class EventProvider(Provider):
    def __init__(self, application):
        self.application = application

    def register(self):
        pass

    def boot(self):
        pass
