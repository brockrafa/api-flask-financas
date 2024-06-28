from src.model.meta import Meta
from src.repository.MetaRepository import *
from src.repository.UsuarioRepository import *
from src.repository.ContaRepository import *
from src.repository.CategoriaRepository import *

def addMeta(dados) -> Meta:
    usuario_id = dados['usuario_id']
    usuario = get_usuario_by_id(usuario_id)
    if not usuario:
        raise Exception("Verifique se o usuario existe.")

    nome_meta = dados['nome_meta']
    valor_meta = dados['valor_meta']
    data_limite = dados['data_limite']
    valor_acumulado = dados['valor_acumulado']
    meta = add_meta(usuario_id,nome_meta,valor_meta,data_limite,valor_acumulado)
    return meta
    
def getMetasByUsuario(id):
    if id == None:
        metas = get_metas()
    else:
        metas = get_metas_by_usuario(id)
    response = []
    if metas:
        for meta in metas:
            response.append(meta.json())
        return response
    return response

def getMetaById(id):
    return  get_meta_by_id(id)

def updateMeta(id_meta,dados):
    if get_meta_by_id(id_meta):
        nome_meta = dados['nome_meta']
        valor_meta = dados['valor_meta']
        data_limite = dados['data_limite']
        valor_acumulado = dados['valor_acumulado']
        return update_meta(id_meta,nome_meta,valor_meta,data_limite,valor_acumulado)
    raise Exception("Meta não encontrada")

def deleteMeta(id):
    if get_meta_by_id(id):
        delete_meta(id)
        return {"mensagem":"Meta excluida com sucesso"}
    raise Exception("Meta informada não encontrada")