from datetime import datetime

from sqlalchemy import DateTime, Column, Boolean, func


class BaseModelMixin(object):
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, onupdate=func.utcnow())
    deleted = Column(Boolean, default=False)
