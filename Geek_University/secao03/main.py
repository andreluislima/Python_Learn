from fastapi import FastAPI

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

if __name__=='__main__':
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, debug=True)