from src.model.usuario import Usuario
from flask_restful import Resource
from sqlAlchemy import banco

def add_usuario( nome: str, email:str, senha:str) -> Usuario:
    """
    Insert a usuario in the database.
    """
    usuario = Usuario(nome,email,senha)
    banco.session.add(usuario)
    banco.session.commit()
    return usuario

def existe_email(email) -> bool:
     usuario = banco.session.query(Usuario).filter_by(email=email).first()
     if usuario:
         return True
     return False
 
def get_usuarios():
     usuarios = banco.session.query(Usuario).all()
     return usuarios
 
def get_usuario_by_id(id):
    return banco.session.query(Usuario).get(id)

def update_usuario(id,nome):
    usuario = banco.session.query(Usuario).get(id)
    usuario.nome = nome
    banco.session.commit()
    return usuario

def delete_usuario(id):
    usuario = banco.session.query(Usuario).get(id)
    if usuario:
        banco.session.delete(usuario)
        banco.session.commit()
        return True
    return False

def autenticar_usuario(email,senha):
    usuario =  banco.session.query(Usuario).filter_by(email=email).first()
    if usuario and usuario.senha == senha:
        return usuario
    else:
        return None
 
# def get_funcionarios() -> sqlalchemy.orm.query.Query:
#     """
#     Get all funcionarios stored in the database.

#     Returns:
#         funcionarios (Funcionario) -- contains all funcionarios registered.
#     """
#     funcionarios = db.session.query(Funcionario).all()
#     return funcionarios

# def get_funcionario(id: int) -> Funcionario:
#     """
#     Get funcionario by id stored in the database.

#     Returns:
#         funcionario (Funcionario) -- contains one funcionario registered.
#     """
#     funcionario = db.session.query(Funcionario).get(id)
#     return funcionario

# def delete_funcionario(id: int):
#     """
#     Delete funcionario by id stored in the database.

#     """
#     funcionario = db.session.query(Funcionario).get(id)
#     db.session.delete(funcionario)
#     db.session.commit()

# def update_funcionario(nome: str, id: int) -> Funcionario:
#     """
#     Insert a Funcionario in the database.
#     """
#     funcionario = db.session.query(Funcionario).get(id)
    
#     funcionario.nome = nome

#     db.session.commit()

#     return funcionario