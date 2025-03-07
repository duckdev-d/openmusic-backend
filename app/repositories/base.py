from typing import Type

from sqlalchemy.orm import Session
from sqlalchemy import Table


class BaseRepo:
    def __init__(self, db: Session, table: Type[Table]):
        self.db = db
        self.table = table

    def get_all(self):
        query = self.db.query(self.table)
        result = query.all()
        return result
