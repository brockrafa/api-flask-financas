from src.model.conta import Conta
from flask_restful import Resource
from sqlAlchemy import banco

def add_conta( usuario_id, nome_conta,saldo_inical):
    conta = Conta(nome_conta,saldo_inical,usuario_id)
    banco.session.add(conta)
    banco.session.commit()
    return conta
 
def get_contas():
     conta = banco.session.query(Conta).all()
     return conta
 
def get_contas_by_usuario(id):
    conta =  banco.session.query(Conta).filter_by(usuario_id=id).all()
    return conta

def get_conta_by_id(id):
    return banco.session.query(Conta).get(id)

def update_conta(id,nome,saldo):
    conta = banco.session.query(Conta).get(id)
    conta.nome_conta = nome
    conta.saldo_inicial = saldo
    banco.session.commit()
    return conta

def update_transacao_conta(transacao,conta_id):
    conta = get_conta_by_id(conta_id)
    if transacao.tipo == 'Despesa':
        conta.saldo_inicial -= transacao.valor
    else:
        conta.saldo_inicial += transacao.valor
        
    return update_conta(conta.conta_id,conta.nome_conta,conta.saldo_inicial)
    
def delete_conta(id):
    conta = banco.session.query(Conta).get(id)
    banco.session.delete(conta)
    banco.session.commit()

