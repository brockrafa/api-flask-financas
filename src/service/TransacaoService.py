from src.model.transacao import Transacao
from src.repository.TransacaoRepository import *
from src.repository.UsuarioRepository import *
from src.repository.ContaRepository import *
from src.repository.CategoriaRepository import *

def addTransacao(dados) -> Transacao:
    usuario_id = dados['usuario_id']
    conta_id = dados['conta_id']
    categoria_id = dados['categoria_id']

    usuario = get_usuario_by_id(usuario_id)
    conta = get_conta_by_id(conta_id)
    categoria = get_categoria_by_id(categoria_id)
    
    if not usuario or not conta or not categoria:
        raise Exception("Verifique se o usuario, conta e categoria existe.")

    valor = dados['valor']
    tipo = dados['tipo']
    descricao = dados['descricao']
    transacao = add_transacao(usuario_id,conta_id,categoria_id,valor,tipo,descricao)
    
    if transacao:
        update_transacao_conta(transacao,conta_id)
    return transacao
    
def getTransacoesByUsuario(id):
    if id == None:
        transacoes = get_transacoes()
    else:
        transacoes = get_transacoes_by_usuario(id)
    response = []
    if transacoes:
        for transacao in transacoes:
            response.append(transacao.json())
        return response
    return response

def getTransacaoById(id):
    return  get_transacao_by_id(id)

def updateTransacao(id_transacao,dados):
    conta_id = dados['conta_id']
    categoria_id = dados['categoria_id']
    conta = get_conta_by_id(conta_id)
    categoria = get_categoria_by_id(categoria_id)
    if not conta or not categoria:
        raise Exception("Verifique se a conta e categoria existem.")
    if get_transacao_by_id(id_transacao):
        valor = dados['valor']
        tipo = dados['tipo']
        descricao = dados['descricao']
        return update_transacao(id_transacao,conta_id,categoria_id,valor,tipo,descricao)
    raise Exception("Transacao não encontrada")

def deleteTransacao(id):
    if get_transacao_by_id(id):
        delete_transacao(id)
        return {"mensagem":"Conta excluida com sucesso"}
    raise Exception("Conta informada não encontrada")