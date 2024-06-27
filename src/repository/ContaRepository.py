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

def update_conta(id,nome):
    conta = banco.session.query(Conta).get(id)
    conta.nome_conta = nome
    banco.session.commit()
    return conta

def delete_conta(id):
    conta = banco.session.query(Conta).get(id)
    banco.session.delete(conta)
    banco.session.commit()

