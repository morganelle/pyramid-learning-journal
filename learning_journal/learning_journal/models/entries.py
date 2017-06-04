from sqlalchemy import (
    Column,
    Integer,
    Unicode,
    DateTime
)

from .meta import Base


class JournalEntry(Base):
    """Journal entry model base class."""
    __tablename__ = 'journal'
    id = Column(Integer, primary_key=True)
    title = Column(Unicode)
    body = Column(Unicode)
    author = Column(Unicode)
    publish_date = Column(DateTime)
