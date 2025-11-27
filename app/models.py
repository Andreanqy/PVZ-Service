from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Optional
from uuid import UUID

from pydantic import RootModel, BaseModel, EmailStr


class Token(RootModel):
    root: str


class Role(Enum):
    employee = 'employee'
    moderator = 'moderator'


class User(BaseModel):
    id: Optional[UUID] = None
    email: EmailStr
    role: Role


class City(Enum):
    Moscow = 'Москва'
    StPetersburg = 'Санкт-Петербург'
    Kazan = 'Казань'


class PVZ(BaseModel):
    id: Optional[UUID] = None
    registrationDate: Optional[datetime] = None
    city: City


class Status(Enum):
    in_progress = 'in_progress'
    close = 'close'


class Reception(BaseModel):
    id: Optional[UUID] = None
    dateTime: datetime
    pvzId: UUID
    status: Status


class Type(Enum):
    electricity = 'электроника'
    clothes = 'одежда'
    shoes = 'обувь'


class Product(BaseModel):
    id: Optional[UUID] = None
    dateTime: Optional[datetime] = None
    type: Type
    receptionId: UUID


class Error(BaseModel):
    message: str
