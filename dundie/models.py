<<<<<<< HEAD
=======
"""..."""

>>>>>>> projeto-dundie-rewards/main
from datetime import datetime
from typing import Optional

from pydantic import condecimal, validator
from sqlmodel import Field, Relationship, SQLModel

from dundie.utils.email import check_valid_email
from dundie.utils.user import generate_simple_password


class InvalidEmailError(Exception):
<<<<<<< HEAD
    ...


class Person(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    email: str = Field(
        nullable=False, index=True, sa_column_kwargs={"unique": True}
    )
=======
    """..."""


class Person(SQLModel, table=True):
    """..."""

    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    email: str = Field(nullable=False, index=True)
>>>>>>> projeto-dundie-rewards/main
    name: str = Field(nullable=False)
    dept: str = Field(nullable=False, index=True)
    role: str = Field(nullable=False)
    currency: str = Field(default="USD")

    balance: "Balance" = Relationship(back_populates="person")
    movement: "Movement" = Relationship(back_populates="person")
    user: "User" = Relationship(back_populates="person")

    @validator("email")
    def validate_email(cls, v: str) -> str:
<<<<<<< HEAD
=======
        """..."""
>>>>>>> projeto-dundie-rewards/main
        if not check_valid_email(v):
            raise InvalidEmailError(f"Invalid email for {v!r}")
        return v

    def __str__(self) -> str:
<<<<<<< HEAD
=======
        """..."""
>>>>>>> projeto-dundie-rewards/main
        return f"{self.name} - {self.role}"


class Balance(SQLModel, table=True):
<<<<<<< HEAD
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    person_id: int = Field(
        foreign_key="person.id",
        sa_column_kwargs={"unique": True}
        # there is only one balance for each person
    )
    value: condecimal(decimal_places=3) = Field(default=0)
=======
    """..."""

    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    person_id: int = Field(foreign_key="person.id")
    value: condecimal(decimal_places=3) = Field(default=0)  # type: ignore
>>>>>>> projeto-dundie-rewards/main

    person: Person = Relationship(back_populates="balance")

    class Config:
<<<<<<< HEAD
=======
        """..."""

>>>>>>> projeto-dundie-rewards/main
        json_encoders = {Person: lambda p: p.pk}


class Movement(SQLModel, table=True):
<<<<<<< HEAD
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    person_id: int = Field(foreign_key="person.id")
    actor: str = Field(nullable=False, index=True)
    value: condecimal(decimal_places=3) = Field(default=0)
=======
    """..."""

    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    person_id: int = Field(foreign_key="person.id")
    actor: str = Field(nullable=False, index=True)
    value: condecimal(decimal_places=3) = Field(default=0)  # type: ignore
>>>>>>> projeto-dundie-rewards/main
    date: datetime = Field(default_factory=lambda: datetime.now())

    person: Person = Relationship(back_populates="movement")

    class Config:
<<<<<<< HEAD
=======
        """..."""

>>>>>>> projeto-dundie-rewards/main
        json_encoders = {Person: lambda p: p.pk}


class User(SQLModel, table=True):
<<<<<<< HEAD
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    person_id: int = Field(
        foreign_key="person.id", sa_column_kwargs={"unique": True}
    )
=======
    """..."""

    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    person_id: int = Field(foreign_key="person.id")
>>>>>>> projeto-dundie-rewards/main
    password: str = Field(default_factory=generate_simple_password)

    person: Person = Relationship(back_populates="user")

    class Config:
<<<<<<< HEAD
=======
        """..."""

>>>>>>> projeto-dundie-rewards/main
        json_encoders = {Person: lambda p: p.pk}
