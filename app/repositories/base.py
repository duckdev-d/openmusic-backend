from typing import TypeVar
from typing import Generic

from sqlalchemy.orm import Session


ModelType = TypeVar('ModelType')


class BaseRepo(Generic[ModelType]):
    def __init__(self, db: Session, entity: type[ModelType]):
        self.db = db
        self.entity = entity

    def get_all(self) -> list[ModelType]:
        query = self.db.query(self.entity)
        result = query.all()
        return result

    def get_by_id(self, id: int) -> ModelType | None:
        return self.db.query(self.entity).where(self.entity.id == id).first()

    def add(self, entity: ModelType) -> ModelType:
        self.db.add(entity)
        self.db.commit()
        return entity

    def delete(self, entity: ModelType) -> None:
        try:
            self.db.delete(entity)
            self.db.commit()
        except:
            raise Exception('Provided value does not exist')
