from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from enum import Enum
from database import Database

app = FastAPI()

database = Database()


@app.get('/usuarios/')
def pegar_usuarios():
    usuarios = database.get_usuarios()
    print('database_service', usuarios)
    return usuarios


@app.get('/usuarios/{id}/')  # DELETE é igual ao get para implementar
def pegar_usuario_pelo_id(id: int):
    if usuario := database.get_usuario_por_id(id):
        print('database_service', usuario)
        return usuario
    return JSONResponse(
        {'error': 'Usuário não encontrado'},
        status_code=404
    )
    

@app.delete('/usuarios/{id}/', status_code=204)
def deletar_usuario_pelo_id(id: int):
    if usuario := database.delete_usuario_por_id(id):
        return usuario
    return JSONResponse(
        {'error': 'Usuário não encontrado'},
        status_code=404
    )


# class PossiveisGeneros(str, Enum):
#     MASCULINO = 'masculino'
#     FEMININO = 'feminino'


class DadosDeEntradaDoUsuario(BaseModel):
    name: str = Field(..., title='Nome do usuário')
    age: int = Field(..., title='Idade do usuário')


@app.post('/usuarios/', status_code=201)
def criar_usuario(usuario: DadosDeEntradaDoUsuario):
    novo_usuario = database.create_usuario(usuario.dict())
    return novo_usuario


@app.put('/usuarios/{id}/')
def atualizar_usuario_pelo_id(
    id: int,
    informacoes_para_atualizar: DadosDeEntradaDoUsuario
):
    if usuario := database.update_usuario_por_id(
        id,
        informacoes_para_atualizar
    ):
        return usuario
    return JSONResponse(
        {'error': 'Usuário não encontrado'},
        status_code=404
    )
