from sqlalchemy.orm import Session


class BaseRepo:
    def __init__(self, db: Session, table: object):
        self.db = db
        self.table = table

    def get_all(self):
        query = self.db.query(self.table)
        result = query.all()
        return result
