from typing import Optional
from pydantic import BaseModel


class Curso(BaseModel):
    id:int
    titulo:str
    aulas:int
    horas:int

