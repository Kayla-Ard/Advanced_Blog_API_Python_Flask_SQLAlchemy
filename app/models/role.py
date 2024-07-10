from app.database import db, Base
from sqlalchemy.orm import Mapped, mapped_column
from typing import List
from app.models.user import User 

class Role(Base):
    __tablename__ = "roles"
    id: Mapped[int] = mapped_column(primary_key=True)
    role_name: Mapped[str] = mapped_column(db.String(255), nullable=False, unique=True)
    users: Mapped[List["User"]] = db.relationship(back_populates="role")
