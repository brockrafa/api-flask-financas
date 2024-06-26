from sqlAlchemy import banco
from sqlalchemy import Column, Integer, ForeignKey, Float, Double, String, DateTime, Text, func
from sqlalchemy.orm import relationship

class Conta(banco.Model):
    __tablename__ = 'conta'
    
    conta_id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey('usuario.usuario_id'), nullable=False)
    nome_conta = Column(String(150), nullable=False)
    saldo_inicial = Column(Double(10,2))
    usuario = relationship("Usuario", back_populates="contas")
    transacoes = relationship("Transacao", back_populates="contas")
    
        
    def __init__(self,nome_conta,saldo_inicial,usuario_id):
        self.usuario_id = usuario_id
        self.nome_conta = nome_conta
        self.saldo_inicial = saldo_inicial
    
    def __init__(self):
        pass
    
    ## Função criada para retornar um json do modelo nas requisições
    def json(self):
        return {
            'conta_id':self.conta_id,
            'nome_conta':self.nome_conta,
            'saldo_inicial':float(self.saldo_inicial),
            'usuario':self.usuario.json()
        }
        
    ## Procurar modelo pelo id
    @classmethod 
    def findById(cls,id):
        return cls.query.get(id)
    
    @classmethod
    def findByUsuarioId(cls, usuario_id):
        return cls.query.filter_by(usuario_id=usuario_id).first()
    
    ## Obter todos os registros do modelo
    @classmethod 
    def getAll(cls):
        return cls.query.all()
    
    ## Salvar modelo no banco
    def save(self):
        banco.session.add(self)
        banco.session.commit()
        
    ## Atualizar modelo
    def update(self):
        banco.session.commit()
    
    ## Deletar modelo
    def delete(self):
        banco.session.delete(self)
        banco.session.commit()