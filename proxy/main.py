from abc import ABC, abstractmethod


class Database(ABC):
    @abstractmethod
    def query(self, sql: str):
        pass


class RealDatabase(Database):
    def query(self, sql: str):
        print(f"Executing query: {sql}")


class DatabaseProxy(Database):
    def __init__(self, has_access: bool):
        self._real_database = RealDatabase()
        self._has_access = has_access

    def query(self, sql: str):
        if self._has_access:
            self._real_database.query(sql)
        else:
            print("Access denied. Query cannot be executed.")


if __name__ == "__main__":
    user_db = DatabaseProxy(has_access=False)
    admin_db = DatabaseProxy(has_access=True)

    user_db.query("SELECT * FROM users")
    admin_db.query("SELECT * FROM users")
