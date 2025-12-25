from typing import Optional
from pydantic import BaseModel


class Curso(BaseModel):
    id:Optional[int] = None
    titulo:str
    aulas:int
    horas:int

cursos = {
    1:{
        "título":"Programação para leigos",
        "aulas":111,
        "horas":58
    },

    2:{
        "título":"Algorítmos e lógica de programação",
        "aulas":87,
        "horas":67
    },
    3:{
        "título":"Programação em C",
        "aulas":92,
        "horas":101
    }
}