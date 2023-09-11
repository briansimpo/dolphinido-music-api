from .Repository import Repository


class FollowingRepository(Repository):

    def get_artists_followed(self, user_id):
        return self.query().with_meta()\
            .where("user_id", user_id)\
            .get()

    def following_exists(self, user_id, artist_id):
        return self.query()\
            .where("user_id", user_id)\
            .where("artist_id", artist_id)\
            .exists()
