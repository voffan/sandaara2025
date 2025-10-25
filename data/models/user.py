from typing import List, TYPE_CHECKING
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from data.models.basemodel import BaseModel

if TYPE_CHECKING:    
    from data.models.pet import Pet
    from data.models.donate import Donate


class User(BaseModel):
    
    __tablename__ = 'users'

    fullname: Mapped[str] = mapped_column(String(250))
    email: Mapped[str] = mapped_column(String(250), unique=True)
    password: Mapped[str] = mapped_column(String(250))
    address: Mapped[str] = mapped_column(String(150))

    pets:Mapped[List["Pet"]] = relationship("Pet", back_populates='owner')
    user_donates: Mapped[List["Donate"]] = relationship("Donate", back_populates='donator')