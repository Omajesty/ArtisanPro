from datetime import datetime
from enum import StrEnum

from sqlalchemy import Column, DateTime, Enum, func, true
from sqlmodel import Field, SQLModel


class UserRole(StrEnum):
    CUSTOMER = "CUSTOMER"
    ARTISAN = "ARTISAN"
    ADMIN = "ADMIN"


class User(SQLModel, table=True):
    # "user" is a reserved word in PostgreSQL, so the table is "users".
    __tablename__ = "users"

    id: int | None = Field(default=None, primary_key=True)
    email: str = Field(max_length=255, unique=True, index=True)
    password_hash: str = Field(max_length=255)
    full_name: str = Field(max_length=120)
    phone: str | None = Field(default=None, max_length=20)

    # Stored as VARCHAR + CHECK constraint, not a native Postgres ENUM type:
    # adding a role later is then a simple migration.
    role: UserRole = Field(
        sa_column=Column(
            Enum(UserRole, name="user_role", native_enum=False, create_constraint=True, length=20),
            nullable=False,
        )
    )
    is_active: bool = Field(default=True, sa_column_kwargs={"server_default": true()})

    # The database fills these in (server_default), always in UTC with time zone.
    created_at: datetime | None = Field(
        default=None,
        sa_column=Column(DateTime(timezone=True), nullable=False, server_default=func.now()),
    )
    updated_at: datetime | None = Field(
        default=None,
        sa_column=Column(
            DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now()
        ),
    )
