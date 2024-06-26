from src.model.categoria import Categoria
from flask_restful import Resource
from sqlAlchemy import banco

def add_categoria( usuario_id, nome_categoria, tipo):
    categoria = Categoria(nome_categoria,tipo,usuario_id)
    banco.session.add(categoria)
    banco.session.commit()
    return categoria
 
def get_categorias():
     categoria = banco.session.query(Categoria).all()
     return categoria
 
def get_categorias_by_usuario(id):
    categoria =  banco.session.query(Categoria).filter_by(usuario_id=id).all()
    return categoria

def get_categoria_by_id(id):
    return banco.session.query(Categoria).get(id)

def update_categoria(id,nome,tipo):
    categoria = banco.session.query(Categoria).get(id)
    categoria.nome_categoria = nome
    categoria.tipo = tipo
    banco.session.commit()
    return categoria

def delete_categoria(id):
    categoria = banco.session.query(Categoria).get(id)
    banco.session.delete(categoria)
    banco.session.commit()

