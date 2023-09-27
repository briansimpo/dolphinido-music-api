"""CreateSongsTable Migration."""

from masoniteorm.migrations import Migration


class CreateSongsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("songs") as table:
            table.uuid('id').primary()
            table.string('title')
            table.string('hash').unique().nullable()
            table.integer('size').nullable()
            table.integer('bitrate').nullable()
            table.integer('duration').nullable()
            table.string('year', 8).nullable()
            table.float('price').nullable()
            table.boolean('is_free').default(True)
            table.boolean('is_published').default(False)
            table.string('file_path').nullable()
            table.string('image_path').nullable()
            table.string('file_url').nullable()
            table.string('image_url').nullable()
            table.text('lyrics').nullable()
            table.uuid('artist_id')
            table.uuid('genre_id').nullable()
            table.uuid('album_id').nullable()
            table.timestamps()

            table.foreign('artist_id').references('id').on('artists').on_delete('cascade')
            table.foreign('genre_id').references('id').on('genres').on_delete('set null')
            table.foreign('album_id').references('id').on('albums').on_delete('set null')



    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("songs")
