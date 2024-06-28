from flask_restful import Resource
from sqlalchemy import Column, Integer, ForeignKey, Float, Double, String, DateTime, Text, func
from sqlAlchemy import banco
from sqlalchemy.orm import relationship
from sqlalchemy.exc import SQLAlchemyError

class Usuario(banco.Model):
    __tablename__ = 'usuario'

    usuario_id = Column(Integer, primary_key=True,autoincrement=True)
    nome = Column(String(150))
    email = Column(String(150), nullable=False)  # Adicione o campo de email
    senha = Column(String(150), nullable=False)
    data_criacao = Column(DateTime, default=func.now())
    
# Relacionamentos
    contas = relationship("Conta", back_populates="usuario")
    categorias = relationship("Categoria", back_populates="usuario")
    metas = relationship("Meta", back_populates="usuario")
    transacoes = relationship("Transacao", back_populates="usuario")

    def __init__(self, nome=None,email=None,senha=None):
        self.nome = nome
        self.email = email
        self.senha = senha
        
    def getAtributes():
        return ["nome","email","senha"]
    
    ## Função criada para retornar um json do modelo nas requisições
    def json(self):
        return {
            'usuario_id':self.usuario_id,
            'nome':self.nome,
            'email':self.email,
            'data_criacao':str(self.data_criacao)
        }