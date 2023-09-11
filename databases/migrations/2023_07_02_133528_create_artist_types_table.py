"""CreateArtistTypesTable Migration."""

from masoniteorm.migrations import Migration


class CreateArtistTypesTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("artist_types") as table:
            table.uuid("id").primary()
            table.string('name')
            table.string('slug').nullable()
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("artist_types")
