from .Repository import Repository


class SongDownloadRepository(Repository):

    def get_downloads(self, user_id):
        return self.query().with_meta()\
            .where("user_id", user_id)\
            .get()

    def count_downloads(self, song_id):
        return self.query().with_meta() \
            .where("song_id", song_id) \
            .sum("download_count") \
            .get()

    def download_exists(self, user_id, song_id) -> bool:
        return self.query()\
            .where("user_id", user_id) \
            .where("song_id", song_id) \
            .exists()

    def get_download(self, user_id, song_id):
        return self.query().with_meta() \
            .where("user_id", user_id) \
            .where("song_id", song_id) \
            .get()
