from .models import Role, City
from pydantic import BaseModel

"""=== Requests ==="""
class DummyLoginRequest(BaseModel):
    role: Role