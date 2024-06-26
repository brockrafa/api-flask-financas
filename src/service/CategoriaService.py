from src.model.usuario import Usuario
from src.model.conta import Conta
from src.repository.CategoriaRepository import *
from src.repository.UsuarioRepository import *

def addCategoria(id,nome,tipo) -> Usuario:
    usuario = get_usuario_by_id(id)
    if not usuario:
        raise Exception("Usuario informado não existe")
    categoria = add_categoria(id,nome,tipo)
    return categoria
    
def getCategoriasByUsuario(id):
    if id == None:
        categorias = get_categorias()
    else:
        categorias = get_categorias_by_usuario(id)
    response = []
    if categorias:
        for categoria in categorias:
            response.append(categoria.json())
        return response
    return categorias

def getCategoriaById(id):
    return  get_categoria_by_id(id)

def updateCategoria(id,dados):
    if 'nome_categoria' in dados and 'tipo' in dados and not dados['tipo'] == '' and not dados['nome_categoria'] == '':
        if get_categoria_by_id(id):
            nome = dados.get("nome_categoria")
            tipo = dados.get("tipo")
            return update_categoria(id,nome,tipo)
        raise Exception("Categoria não encontrada")
    raise Exception("Os campos nome_categoria e tipo sao obrigatorios")

def deleteCategoria(id):
    if get_categoria_by_id(id):
        delete_categoria(id)
        return {"mensagem":"Categoria excluida com sucesso"}
    raise Exception("Categoria informada não encontrada")