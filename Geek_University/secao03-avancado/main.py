from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status
from fastapi.responses import JSONResponse
from fastapi import Response
from fastapi import Path

from typing import Dict, List

from models import Curso
from models import cursos


app = FastAPI(
    title="API de Cursos da Geek University",
    version='0.0.1',
    description='Uma API para estudo do FastAPI'
    )


@app.get('/cursos', 
            description='Retorna todos os cursos ou uma lista vazia', 
            summary='Retorna todos os cursos',
            # response_model=Dict[int, Curso]
            response_model = List[Curso], 
            response_description='Curso encontrado com sucesso.'
            )
async def get_cursos():
    return cursos


@app.get('/cursos/{curso_id}')
async def get_curso_by_id(curso_id:int = Path(default=None, title='ID do Curso', description='Deve ser entre 1 e 2', gt=0, lt=3)):
    try:
        curso = cursos[curso_id]
        return curso
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado.'
        )


@app.post('/cursos', status_code=status.HTTP_201_CREATED, response_model=Curso)
async def post_curso(curso: Curso):
    next_id: int = len(cursos) + 1
    curso.id = next_id
    cursos.append(curso)

    return curso

@app.put('/cursos/{curso_id}')
async def put_curso(curso_id:int, curso: Curso):
    
    if curso_id in cursos:
        cursos[curso_id] = curso
        del curso.id

        return curso
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f'Curso não encontrado para o id: {curso_id}'
        )


@app.delete('/cursos/{curso_id}')
async def delete_curso(curso_id:int):
    if curso_id in cursos:
        del cursos[curso_id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Não existe um curso com o id {curso_id}."
        )


if __name__=='__main__':
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, debug=True, reload=True)