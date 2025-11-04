from typing import List, TYPE_CHECKING
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from data.models.base import BaseModel
from data.models.user import User
from data.models.species import Species

if TYPE_CHECKING:
    from data.models.donate import Donate


class Pet(BaseModel):
    
    __tablename__ = 'pets'

    name: Mapped[str] = mapped_column(String(250))
    needed: Mapped[int] = mapped_column(Integer)
    balance: Mapped[int] = mapped_column(Integer, default=0)
    file: Mapped[str] = mapped_column(String(250), server_default="", default="")

    species_id: Mapped[int] = mapped_column(ForeignKey("species.id"))
    species: Mapped["Species"] = relationship('Species', back_populates='animals')

    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    owner: Mapped["User"] = relationship("User", back_populates="pets")

    pet_donates: Mapped[List["Donate"]] = relationship('Donate', back_populates='pet')

    def __str__(self):
        return self.species.name + ' ' + self.name + ' ' + self.owner.fullname
