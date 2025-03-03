from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped

from core.database import Base


class IdMixin(object):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)


class CreatedAtMixin(object):
    created_at: Mapped[datetime] = mapped_column()
