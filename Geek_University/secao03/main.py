from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status

app = FastAPI()

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
    }
}

@app.get('/curso')
async def get_cursos():
    return cursos

## SEM tratamento de exceção
# @app.get('/curso/{curso_id}')
# async def get_curso(curso_id:int): ## curso_id:int -> Declarando que o valor do id deve ser inteiro. 
#                                    ## Caso não seja, o fastapi irá tratar o erro.
#     curso = cursos[curso_id]
#     curso.update({"id":curso_id})
    
#     return curso

## COM tratamento de exceção
@app.get('/curso/{curso_id}')
async def get_curso_by_id(curso_id:int):
    try:
        curso = cursos[curso_id]
        return curso
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado.'
        )

if __name__=='__main__':
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, debug=True, reload=True)