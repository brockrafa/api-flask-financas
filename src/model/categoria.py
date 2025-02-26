from sqlAlchemy import banco
from sqlalchemy import Column, Integer, ForeignKey, Float, Double, String, DateTime, Text, func
from sqlalchemy.orm import relationship

class Categoria(banco.Model):
    __tablename__ = 'categoria'
    
    categoria_id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey('usuario.usuario_id', ondelete='CASCADE'), nullable=False)
    nome_categoria = Column(String(150), nullable=False)
    tipo = Column(String(150), nullable=False)
    
    usuario = relationship("Usuario", back_populates="categorias")
    transacoes = relationship('Transacao', back_populates='categorias', cascade='all, delete-orphan', passive_deletes=True)
    
    def __init__(self,nome_categoria=None, tipo=None, usuario_id=None):
        self.usuario_id = usuario_id
        self.nome_categoria = nome_categoria
        self.tipo = tipo
    
    
    ## Função criada para retornar um json do modelo nas requisições
    def json(self):
        return {
            'categoria_id':self.categoria_id,
            'nome_categoria':self.nome_categoria,
            'tipo':self.tipo,
            'usuario':self.usuario.json()
        }

    
