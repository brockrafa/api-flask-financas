from sqlAlchemy import banco
from sqlalchemy import Column, Integer, ForeignKey, Float, Double, String, DateTime, Text, func
from sqlalchemy.orm import relationship

class Conta(banco.Model):
    __tablename__ = 'conta'
    
    conta_id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey('usuario.usuario_id'), nullable=False)
    nome_conta = Column(String(150), nullable=False)
    saldo_inicial = Column(Float)
    usuario = relationship("Usuario", back_populates="contas")
    transacoes = relationship("Transacao", back_populates="contas")
    
        
    def __init__(self,nome_conta=None,saldo_inicial=None,usuario_id=None):
        self.usuario_id = usuario_id
        self.nome_conta = nome_conta
        self.saldo_inicial = saldo_inicial
    
    ## Função criada para retornar um json do modelo nas requisições
    def json(self):
        return {
            'conta_id':self.conta_id,
            'nome_conta':self.nome_conta,
            'saldo_inicial':float(f"{self.saldo_inicial:.2f}"),
            'usuario':self.usuario.json()
        }
    