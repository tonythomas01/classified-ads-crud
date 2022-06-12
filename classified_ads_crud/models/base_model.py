from datetime import datetime

from sqlalchemy import DateTime, Column, Boolean


class BaseModelMixin(object):
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, onupdate=datetime.utcnow())
    deleted = Column(Boolean, default=False)
