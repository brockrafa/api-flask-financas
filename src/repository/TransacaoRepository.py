from src.model.transacao import Transacao
from flask_restful import Resource
from sqlAlchemy import banco

def add_transacao( usuario_id, conta_id, categoria_id, valor, tipo, descricao):

    conta = Transacao(usuario_id, conta_id, categoria_id, valor, tipo, descricao)
    banco.session.add(conta)
    banco.session.commit()
    return conta
 
def get_transacoes():
     transacao = banco.session.query(Transacao).all()
     return transacao
 
def get_transacoes_by_usuario(id):
    transacao =  banco.session.query(Transacao).filter_by(usuario_id=id).all()
    return transacao

def get_transacao_by_id(id):
    return banco.session.query(Transacao).get(id)

def update_transacao(id_transacao,conta_id,categoria_id,valor,tipo,descricao):
    transacao = banco.session.query(Transacao).get(id_transacao)
    transacao.conta_id = conta_id
    transacao.categoria_id = categoria_id
    transacao.valor = valor
    transacao.tipo = tipo
    transacao.descricao = descricao
    banco.session.commit()
    return transacao

def delete_transacao(id):
    transacao = banco.session.query(Transacao).get(id)
    banco.session.delete(transacao)
    banco.session.commit()

