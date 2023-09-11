from .Repository import Repository


class AlbumDownloadRepository(Repository):

    def get_downloads(self, user_id):
        return self.query().with_meta()\
            .where("user_id", user_id)\
            .get()

    def count_downloads(self, album_id):
        return self.query().with_meta() \
            .where("album_id", album_id) \
            .sum("download_count") \
            .get()

    def download_exists(self, user_id, album_id) -> bool:
        return self.query() \
            .where("user_id", user_id) \
            .where("album_id", album_id) \
            .exists()

    def get_download(self, user_id, album_id):
        return self.query().with_meta() \
            .where("user_id", user_id) \
            .where("album_id", album_id) \
            .get()
