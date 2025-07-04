from typing import Literal

from pydantic import BaseModel, HttpUrl


class Link(BaseModel):
    category: Literal["Scenery", "Charts", "Briefing", "GSX Config"] | None = None
    name: str
    url: HttpUrl


class Airport(BaseModel):
    icao: str
    links: list[Link]


class AirportData(BaseModel):
    airports: list[Airport]
