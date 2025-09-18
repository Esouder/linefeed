from pydantic import BaseModel


class ApiConfig(BaseModel):
    port: int
    host: str
