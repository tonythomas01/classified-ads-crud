from sqlalchemy import CheckConstraint, Column, Integer, String, Text

from classified_ads_crud.database import Base
from classified_ads_crud.models.base_model import BaseModelMixin


class Ad(BaseModelMixin, Base):
    __tablename__ = "ads"

    id = Column(Integer, primary_key=True, autoincrement=True)
    subject = Column(String(60), unique=False, nullable=False)
    body = Column(Text(3000), nullable=False)
    email = Column(String(320), nullable=False)
    price = Column(Integer, nullable=True)  # Optional
    currency = Column(String(5), nullable=True)

    __table_args__ = (CheckConstraint(price >= 0, name="check_positive_price"), {})

    def __repr__(self) -> str:
        return f"<Ad {self.id}>"
