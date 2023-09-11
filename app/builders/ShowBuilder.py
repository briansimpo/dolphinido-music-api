from masoniteorm.query import QueryBuilder


class ShowBuilder(QueryBuilder):

    def with_meta(self):
        return self.left_join("artists", "shows.artist_id", "=", "artists.id") \
            .select(
				"shows.*", 
				"artists.name as artist"
			)
