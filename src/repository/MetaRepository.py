from src.model.meta import Meta
from flask_restful import Resource
from sqlAlchemy import banco

def add_meta(usuario_id,nome_meta,valor_meta,data_limite,valor_acumulado):
    meta = Meta(usuario_id,nome_meta,valor_meta,data_limite,valor_acumulado)
    banco.session.add(meta)
    banco.session.commit()
    return meta
 
def get_metas():
     meta = banco.session.query(Meta).all()
     return meta
 
def get_metas_by_usuario(id):
    meta =  banco.session.query(Meta).filter_by(usuario_id=id).all()
    return meta

def get_meta_by_id(id):
    return banco.session.query(Meta).get(id)

def update_meta(id,nome_meta,valor_meta,data_limite,valor_acumulado):
    meta = banco.session.query(Meta).get(id)
    meta.nome_meta = nome_meta
    meta.valor_meta = valor_meta
    meta.data_limite = data_limite
    meta.valor_acumulado = valor_acumulado
    banco.session.commit()
    return meta

def delete_meta(id):
    meta = banco.session.query(Meta).get(id)
    banco.session.delete(meta)
    banco.session.commit()

