class EmptyMixin:

    def empty(self):
        data = { 
            "data": [], 
            "meta": {"last_page": 1 } 
        }
        return data
        