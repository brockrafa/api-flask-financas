from src.model.usuario import Usuario
from src.model.conta import Conta
from src.repository.ContaRepository import *
from src.repository.UsuarioRepository import *

def addConta(id,nome) -> Conta:
    usuario = get_usuario_by_id(id)
    if not usuario:
        raise Exception("Usuario informado não existe")
    saldo_inical = 0.0
    conta = add_conta(id,nome,saldo_inical)
    return conta
    
def getContasByUsuario(id):
    if id == None:
        contas = get_contas()
    else:
        contas = get_contas_by_usuario(id)
    response = []
    if contas:
        for conta in contas:
            response.append(conta.json())
        return response
    return contas

def getContaById(id):
    return  get_conta_by_id(id)

def updateCategoria(id,dados):
    if 'nome_conta' in dados and not dados['nome_conta'] == '':
        if get_conta_by_id(id):
            nome = dados.get("nome_conta")
            return update_conta(id,nome)
        raise Exception("Conta não encontrada")
    raise Exception("Os campos nome_conta é obrigatorio")

def deleteConta(id):
    if get_conta_by_id(id):
        delete_conta(id)
        return {"mensagem":"Conta excluida com sucesso"}
    raise Exception("Conta informada não encontrada")