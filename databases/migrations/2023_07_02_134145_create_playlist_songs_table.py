"""CreatePlaylistsTable Migration."""

from masoniteorm.migrations import Migration


class CreatePlaylistSongsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("playlist_songs") as table:
            table.increments("id")
            table.uuid('playlist_id')
            table.uuid('song_id')
            table.timestamps()

            table.foreign('playlist_id').references('id').on('playlists').on_delete('cascade')
            table.foreign('song_id').references('id').on('songs').on_delete('cascade')


    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("playlist_songs")
