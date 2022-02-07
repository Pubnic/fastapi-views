from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from enum import Enum

app = FastAPI()

database = {
    'usuarios': [{'id': 1, 'name': 'John', 'age': 30}, {'id': 2, 'name': 'Doe', 'age': 27}],
    'post': [
        {'id': 1, 'title': 'Hello', 'content': 'World', 'author_id': 1},
    ]
}


@app.get('/usuarios/')
def pegar_usuarios():
    return database['usuarios']


@app.get('/usuarios/{id}/')  # DELETE é igual ao get para implementar
def pegar_usuario_pelo_id(id: int):
    for usuario in database['usuarios']:
        if usuario['id'] == id:
            return usuario
    return JSONResponse(
        {'error': 'Usuário não encontrado'},
        status_code=404
    )
    
    
@app.delete('/usuarios/{id}/', status_code=204)
def deletar_usuario_pelo_id(id: int):
    pass


class PossiveisGeneros(str, Enum):
    MASCULINO = 'masculino'
    FEMININO = 'feminino'


class DadosDeEntradaDoUsuario(BaseModel):
    name: str = Field(..., title='Nome do usuário')
    age: int = Field(..., title='Idade do usuário')
    gender: PossiveisGeneros


@app.post('/usuarios/', status_code=201)
def criar_usuario(usuario: DadosDeEntradaDoUsuario):
    proximo_id = 1
    for usuario_do_banco in database['usuarios']:
        if usuario_do_banco['id'] == proximo_id:
            proximo_id += 1
    novo_usuario = {
        **usuario.dict(),
        'id': proximo_id
    }
    database['usuarios'].append(novo_usuario)
    return novo_usuario


@app.put('/usuarios/{id}/')
def atualizar_usuario_pelo_id(
    informacoes_para_atualizar: DadosDeEntradaDoUsuario
):
    pass  # For procurando pelo usuario com aquele, substituir as informação, sem modificar o id