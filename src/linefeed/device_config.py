from pydantic import BaseModel


class DeviceConfig(BaseModel):
    location: str
