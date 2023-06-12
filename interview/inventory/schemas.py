from typing import List
from decimal import Decimal
from pydantic import BaseModel


class InventoryMetaData(BaseModel):
    year: int
    actors: List[str]
    imdb_rating: Decimal
    rotten_tomatoes_rating: int
