from sqlalchemy import Column, Integer, String, Float
from app.DB.base import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)
    image_url = Column(String)
    seller_id = Column(Integer, nullable=False)
