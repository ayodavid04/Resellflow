from sqlalchemy import Column, Integer, String, Float
from app.DB.base import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    buyer_email = Column(String, nullable=False)
    total_price = Column(Float, nullable=False)
    products = Column(String, nullable=False)  # For MVP, store as comma-separated string or JSON
    seller_id = Column(Integer, nullable=False)
