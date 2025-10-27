from typing import List, TYPE_CHECKING
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from data.models.base import BaseModel

if TYPE_CHECKING:
    from data.models.pet import Pet


class Species(BaseModel):
    __tablename__ = 'species'

    name: Mapped[str] = mapped_column(String(100))

    animals: Mapped[List["Pet"]] = relationship('Pet', back_populates='species')

    def __str__(self):
        return self.name