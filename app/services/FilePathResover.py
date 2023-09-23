import os
import uuid
from app.config.uploads import STORAGE_DIR, PLACEHOLDER

class FilePathResover:
    
    def resolve(self, file_path: str):
        return os.path.join(STORAGE_DIR, file_path)
    
    def placeholder(self):
        return self.resolve(PLACEHOLDER)
    
    def random_name(self):
        name = uuid.uuid4()
        return name
