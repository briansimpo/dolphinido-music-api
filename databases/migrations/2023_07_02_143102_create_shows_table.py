"""CreateShowsTable Migration."""

from masoniteorm.migrations import Migration


class CreateShowsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("shows") as table:
            table.uuid('id').primary()
            table.string('title')
            table.text('description').nullable()
            table.string('country').nullable()
            table.string('venue')
            table.string('city').nullable()
            table.string('contact_email').nullable()
            table.string('contact_number').nullable()
            table.date('event_date')
            table.string('event_time')
            table.integer('ticket_price').nullable()
            table.integer('seats').nullable()
            table.boolean('is_free').default(True)
            table.boolean('is_public').default(True)
            table.boolean('is_published').default(False)
            table.string('image_path').nullable()
            table.string('image_url').nullable()
            table.uuid('artist_id')
            table.timestamps()

            table.foreign('artist_id').references('id').on('artists').on_delete('cascade')


    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("shows")
