"""CreateAlbumReleasesTable Migration."""

from masoniteorm.migrations import Migration


class CreateAlbumReleasesTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("album_releases") as table:
            table.uuid("id").primary()
            table.string('name')
            table.string('slug').nullable()
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("album_releases")
