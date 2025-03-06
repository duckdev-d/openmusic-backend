from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped


class IdMixin:
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)


class CreatedAtMixin:
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
