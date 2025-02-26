from sqlAlchemy import banco
from sqlalchemy import Column, Integer, ForeignKey, Float, Double, String, DateTime, Text, func
from sqlalchemy.orm import relationship

class Transacao(banco.Model):
    __tablename__ = 'transacao'
    
    transacao_id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey('usuario.usuario_id'), nullable=False)
    conta_id = Column(Integer, ForeignKey('conta.conta_id'), nullable=False)
    categoria_id = Column(Integer, ForeignKey('categoria.categoria_id', ondelete='CASCADE'), nullable=False)
    valor = Column(Float, nullable=False)
    tipo = Column(String(50), nullable=False)
    data = Column(DateTime, default=func.now()) 
    descricao = Column(Text, nullable=True)
    

    usuario = relationship("Usuario", back_populates="transacoes")
    contas = relationship("Conta", back_populates="transacoes")
    categorias = relationship("Categoria", back_populates="transacoes")
    
    def __init__(self, usuario_id=None, conta_id=None, categoria_id=None, valor=None, tipo=None, descricao=None):
        self.usuario_id = usuario_id
        self.conta_id = conta_id
        self.categoria_id = categoria_id
        self.valor = valor
        self.tipo = tipo
        self.descricao = descricao

    ## Função criada para retornar um json do modelo nas requisições
    def json(self):
        return {
            'transacao_id':self.transacao_id,
            'valor':float(self.valor),
            'tipo':self.tipo,
            'data':str(self.data),
            'descricao':self.descricao,
            'usuario':{'id': self.usuario_id, 'nome':str(self.usuario.nome)},
            'conta':self.conta_id,
            'categoria':self.categorias.nome_categoria
        }
        
    