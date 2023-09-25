import importlib
import re
from abc import ABC
from masoniteorm.query import QueryBuilder
from masoniteorm.collection import Collection


class Repository(ABC):
    
    def __init__(self) -> None:
        super().__init__()
        self.__load_model()

    def get_all(self) -> Collection:
        return self.query().with_meta().get()
    
    def get_list(self, limit: int = 20):
        return self.query().with_meta().paginate(limit)
    
    def get_by_id(self, id) -> any:
        return self.query().with_meta().find(record_id=id)

    def delete(self, id):
        return self.query().where('id', id).delete()

    def delete_many(self, ids):
        return self.query().where_in('id', ids).delete()
    
    def get_by_ids(self, ids: list) -> Collection:
        return self.query().with_meta().where_in('id', ids).get()
    
    def query(self) -> QueryBuilder:
        return self.model().query()
    
    def count(self) -> int:
        return self.model.count()

    def __load_model(self):
        model_path, model_name = self.__guess_model_class()
        model_module = Repository.__get_module(model_path)
        self.model = getattr(model_module, model_name)

    def __guess_model_class(self):
        base_name = re.sub(r'app.repositories.', '', self.__class__.__name__)
        class_name = re.sub(r'Repository', '', base_name)
        model_class = f"app.models.{class_name}"
        return model_class, class_name

    @staticmethod
    def __get_module(module_path):
        return importlib.import_module(module_path)


        