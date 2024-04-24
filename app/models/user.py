from sqlalchemy import BigInteger
from sqlalchemy.orm import mapped_column, Mapped

from app.database import Base


class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True)
    telegram_id: Mapped[int] = mapped_column(BigInteger(), nullable=False)