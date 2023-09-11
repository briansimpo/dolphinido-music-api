"""CreateFavouritesTable Migration."""

from masoniteorm.migrations import Migration


class CreateAlbumLikesTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("album_likes") as table:
            table.increments("id")
            table.uuid('user_id')
            table.uuid('album_id')
            table.timestamps()

            table.foreign('user_id').references('id').on('users').on_delete('cascade')
            table.foreign('album_id').references('id').on('albums').on_delete('cascade')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("album_likes")
