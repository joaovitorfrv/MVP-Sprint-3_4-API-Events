from sqlalchemy import Column, Integer, String, Boolean, DateTime, Date
from datetime import datetime
from model import Base

class Event(Base):
    # Define o nome da table
    __tablename__ = 'event_list'

    id:int = Column('event_id',Integer, primary_key = True)
    title:str = Column('event_title',String(200))
    notes:str = Column('event_notes', String(500))
    date:str = Column('event_date', String(20))
    hour:str = Column('event_hour', String(20))
    city:str = Column('event_city', String(100))

