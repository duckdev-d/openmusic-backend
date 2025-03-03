from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import Table
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import func
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from core.database import Base
from models.mixins import IdMixin
from models.mixins import CreatedAtMixin


class User(IdMixin, CreatedAtMixin, Base):
    __tablename__ = 'users'

    username: Mapped[str]
    password_hash: Mapped[str]
    is_admin: Mapped[bool] = mapped_column(default=False)
