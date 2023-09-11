from .Repository import Repository


class AlbumLikeRepository(Repository):

    def get_likes(self, user_id):
        return self.query().with_meta()\
            .where("user_id", user_id)\
            .get()

    def count_likes(self, album_id):
        return self.query()\
            .where("album_id", album_id)\
            .count()

    def like_exists(self, user_id, album_id):
        return self.query()\
            .where("user_id", user_id)\
            .where("album_id", album_id)\
            .exists()
