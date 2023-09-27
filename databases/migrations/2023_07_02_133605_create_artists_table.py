"""CreateArtistsTable Migration."""

from masoniteorm.migrations import Migration


class CreateArtistsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("artists") as table:
            table.uuid("id").primary()
            table.string('name')
            table.date('birthday').nullable()
            table.string('country').nullable()
            table.string('city').nullable()
            table.text('bio').nullable()
            table.string('image_path').nullable()
            table.string('image_url').nullable()
            table.uuid('artist_type_id')
            table.timestamps()

            table.foreign('id').references('id').on('users').on_delete('cascade')
            table.foreign('artist_type_id').references('id').on('artist_types').on_delete('restrict')

            

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("artists")
