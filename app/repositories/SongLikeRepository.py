from .Repository import Repository


class SongLikeRepository(Repository):

    def get_likes(self, user_id):
        return self.query().with_meta()\
            .where("user_id", user_id)\
            .get()

    def count_likes(self, song_id):
        return self.query()\
            .where("song_id", song_id)\
            .count()

    def like_exists(self, user_id, song_id):
        return self.query()\
            .where("user_id", user_id)\
            .where("song_id", song_id)\
            .exists()
