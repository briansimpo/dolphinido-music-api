from masoniteorm.query import QueryBuilder


class ArtistBuilder(QueryBuilder):

    def with_meta(self):
        return self.left_join("artist_types", "artists.artist_type_id", "=", "artist_types.id")\
            .left_join("users", "artists.id", "=", "users.id")\
            .select(
                "artists.*",
                "users.email",
                "artist_types.name as artist_type"
            )
