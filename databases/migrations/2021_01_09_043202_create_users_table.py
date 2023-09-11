from masoniteorm.migrations import Migration


class CreateUsersTable(Migration):
    def up(self):
        """Run the migrations."""
        with self.schema.create("users") as table:
            table.uuid("id").primary()
            table.string("name")
            table.string("email").unique()
            table.string("password")
            table.boolean("is_admin").default(False)
            table.boolean("is_artist").default(False)
            table.boolean("is_fan").default(True)
            table.string("profile_image").nullable()
            table.string("remember_token").nullable()
            table.timestamp("verified_at").nullable()
            table.timestamps()
            table.soft_deletes()

    def down(self):
        """Revert the migrations."""
        self.schema.drop("users")
