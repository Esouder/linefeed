from pydantic import BaseModel
from typing import Literal


class DeviceConfig(BaseModel):
    location: str
