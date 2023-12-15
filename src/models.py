from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import UUID
from uuid import uuid4
from datetime import datetime
from src.db import Base


class User(Base):
    """
    The users' auth model
    """

    __tablename__ = "users"
    id: Mapped[str] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid4()
    )
    username: Mapped[str] = mapped_column(nullable=True)
    first_name:Mapped[str] = mapped_column(nullable=True)
    last_name:Mapped[str] = mapped_column(nullable=True)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    verified: Mapped[bool] = mapped_column(default=False)

    def __str__(self):
        return f"<User {self.email}>"
