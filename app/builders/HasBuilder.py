from masoniteorm.query import QueryBuilder


class HasBuilder:

    def new_builder(self, builder) -> QueryBuilder:
        self.builder = builder(
            connection=self.__connection__,
            table=self.get_table_name(),
            connection_details=self.get_connection_details(),
            model=self,
            scopes=self._scopes.get(self.__class__),
            dry=self.__dry__,
        )
        return self.builder.select(*self.__selects__)
