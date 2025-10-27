from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column


class BaseModel(DeclarativeBase):
    __abstract__ = True  # mark this as an abstract base class

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)