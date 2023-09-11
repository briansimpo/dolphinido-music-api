from .Repository import Repository


class UserRepository(Repository):
	
	def get_by_email(self, email: str):
		return self.query()\
            .where("users.email", email)\
            .first()

	def user_exists(self, email: str):
		return self.query()\
            .where("users.email", email)\
            .exists()
