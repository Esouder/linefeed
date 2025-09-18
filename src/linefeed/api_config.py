from pydantic import BaseModel


class ApiConfig(BaseModel):
    port: int
    host: str = "127.0.0.1"
