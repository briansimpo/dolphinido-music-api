from masoniteorm.query import QueryBuilder


class ShowPerformerBuilder(QueryBuilder):

    def with_meta(self):
        return self.left_join("artists", "shows.artist_id", "=", "artists.id") \
            .select(
                "artists.*",
                "show_performers.show_id",
                "show_performers.artist_id"
            )
