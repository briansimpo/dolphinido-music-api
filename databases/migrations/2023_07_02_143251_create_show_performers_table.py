"""CreateShowPerformersTable Migration."""

from masoniteorm.migrations import Migration


class CreateShowPerformersTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("show_performers") as table:
            table.increments("id")
            table.uuid('show_id')
            table.uuid('artist_id')
            table.timestamps()

            table.foreign('show_id').references('id').on('shows').on_delete('cascade')
            table.foreign('artist_id').references('id').on('artists').on_delete('cascade')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("show_performers")
