"""CreateGenresTable Migration."""

from masoniteorm.migrations import Migration


class CreateGenresTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("genres") as table:
            table.uuid("id").primary()
            table.string('name')
            table.string('slug').nullable()
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("genres")
