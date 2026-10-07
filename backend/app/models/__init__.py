from sqlmodel import SQLModel

# Predictable constraint names, e.g. "uq_users_email", "fk_quotes_job_id_jobs".
# Must be set before any model class is defined (that's why it's first in this file).
# Migrations need stable names to drop or change a constraint later.
SQLModel.metadata.naming_convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}

# Every model is imported here so Alembic sees all tables.
from app.models.user import User, UserRole  # noqa: E402

__all__ = ["User", "UserRole"]
