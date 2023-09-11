from masoniteorm.query import QueryBuilder


class FollowingBuilder(QueryBuilder):

    def with_meta(self):
        return self.left_join("artists", "followings.artist_id", "=", "artists.id") \
            .select(
                "artists.*",
                "followings.user_id",
                "followings.artist_id",
            )
