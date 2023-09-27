
from app.filters import Filter


class ShowFilter(Filter):
    
    def __init__(self) -> None:
        super().__init__()

    def columns(self) -> list:
        return [
            "shows.id", 
            "shows.title", 
            "shows.venue", 
            "shows.description", 
            "shows.country", 
            "shows.city", 
            "shows.contact_email", 
            "shows.contact_number", 
            "shows.ticket_price", 
            "shows.seats", 
            "shows.event_date", 
            "shows.event_time", 
            "shows.is_free", 
            "shows.is_public", 
            "shows.is_published", 
            "shows.image_url"
        ]

    def process(self):

        return self.builder.table("albums") \
            .select(self.columns()) \
            .when(self.filters, lambda query: query.where(self.filters) ) \
            .when(self.sort_by, lambda query: query.order_by(self.sort_by) ) \
            .paginate(self.per_page, self.page)
