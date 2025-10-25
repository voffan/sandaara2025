from typing import List, TYPE_CHECKING
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from data.models.basemodel import BaseModel
from data.models.user import User

if TYPE_CHECKING:
    from data.models.donate import Donate


class Pet(BaseModel):
    
    __tablename__ = 'pets'

    name: Mapped[str] = mapped_column(String(250))
    needed: Mapped[int] = mapped_column(Integer)
    balance: Mapped[int] = mapped_column(Integer)

    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    owner: Mapped[User] = relationship("User", back_populates="pets")

    pet_donates: Mapped[List["Donate"]] = relationship('Donate', back_populates='pet')
