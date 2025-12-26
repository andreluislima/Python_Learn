from sqlalchemy import Column, Integer, String
from core.database import DBBaseModel

class CursoModel(DBBaseModel):
    __tablename__ = "cursos"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    aulas = Column(Integer, nullable=False)
    horas = Column(Integer, nullable=False)
