from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, JSON, create_engine
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class TranslationTask(Base):
    __tablename__ = "translation_tasks"
    
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    languages = Column(String, nullable=False)
    status = Column(String, default="in progress", nullable=False)
    translation = Column(JSON, default={})
    # created_at = Column(DateTime, default=datetime.utcnow)
    # updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)