from pydantic import BaseModel


class Stand(BaseModel):
    icao: str
    name: str
    lat: float | list[float]
    lon: float | list[float]
