from .Repository import Repository


class SongPlayRepository(Repository):


    def get_plays(self, user_id):
        return self.query().with_meta()\
            .where("user_id", user_id)\
            .get()

    def count_plays(self, song_id):
        return self.query().with_meta()\
            .where("song_id", song_id)\
            .sum("play_count") \
            .get()

    def play_exists(self, user_id, song_id) -> bool:
        return self.query() \
            .where("user_id", user_id) \
            .where("song_id", song_id) \
            .exists()

    def get_play(self, user_id, song_id):
        return self.query().with_meta() \
            .where("user_id", user_id) \
            .where("song_id", song_id) \
            .get()
    
