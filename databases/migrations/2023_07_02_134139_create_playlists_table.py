"""CreatePlaylistsTable Migration."""

from masoniteorm.migrations import Migration


class CreatePlaylistsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("playlists") as table:
            table.uuid("id").primary()
            table.string('name')
            table.uuid('user_id')
            table.timestamps()

            table.foreign('user_id').references('id').on('users').on_delete('cascade')
           

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("playlists")
