from masonite.controllers import Controller
from masonite.response import Response
from app.utils.helpers import get_country_list
from app.utils.helpers import get_year_range

class UtilityController(Controller):

    def country_list(self, response: Response):
        countries = list()
        for (key, country) in get_country_list():
            countries.append(country)
        
        return response.json(countries)
    
    def year_list(self, response: Response):
        year_range =  get_year_range()
        return response.json(year_range)
