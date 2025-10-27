from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from data.models.base import BaseModel
from data.models.user import User
from data.models.pet import Pet


class Donate(BaseModel):
    
    __tablename__ = 'donates'

    value: Mapped[int] = mapped_column(Integer)

    pet_id: Mapped[int] = mapped_column(ForeignKey("pets.id"))
    pet: Mapped["Pet"] = relationship("Pet", back_populates="pet_donates")

    donator_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    donator: Mapped["User"] = relationship("User", back_populates="user_donates")