"""CreateFollowingsTable Migration."""

from masoniteorm.migrations import Migration


class CreateFollowingsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("followings") as table:
            table.increments("id")
            table.uuid('user_id')
            table.uuid('artist_id')
            table.timestamps()

            table.foreign('user_id').references('id').on('users').on_delete('cascade')
            table.foreign('artist_id').references('id').on('artists').on_delete('cascade')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("followings")
