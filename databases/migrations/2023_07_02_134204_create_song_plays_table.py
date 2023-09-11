"""CreateStreamsTable Migration."""

from masoniteorm.migrations import Migration


class CreateSongPlaysTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("song_plays") as table:
            table.increments("id")
            table.uuid('user_id')
            table.uuid('song_id')
            table.integer('play_count')
            table.timestamp('last_played_at')
            table.timestamps()

            table.foreign('user_id').references('id').on('users').on_delete('cascade')
            table.foreign('song_id').references('id').on('songs').on_delete('cascade')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("song_plays")
