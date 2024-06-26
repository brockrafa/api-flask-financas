from sqlAlchemy import banco
from sqlalchemy import Column, Integer, ForeignKey, Float, Double, String, DateTime, Text, func
from sqlalchemy.orm import relationship

class Transacao(banco.Model):
    __tablename__ = 'transacao'
    
    transacao_id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey('usuario.usuario_id'), nullable=False)
    conta_id = Column(Integer, ForeignKey('conta.conta_id'), nullable=False)
    categoria_id = Column(Integer, ForeignKey('categoria.categoria_id', ondelete='CASCADE'), nullable=False)
    valor = Column(Double(10,2), nullable=False)
    tipo = Column(String(50), nullable=False)
    data = Column(DateTime, default=func.now()) 
    descricao = Column(Text, nullable=True)
    

    usuario = relationship("Usuario", back_populates="transacoes")
    contas = relationship("Conta", back_populates="transacoes")
    categorias = relationship("Categoria", back_populates="transacoes")
    
    def __init__(self, usuario_id, conta_id, categoria_id, valor, tipo, descricao):
        self.usuario_id = usuario_id
        self.conta_id = conta_id
        self.categoria_id = categoria_id
        self.valor = valor
        self.tipo = tipo
        self.descricao = descricao
    
    def __init__(self):
        pass
    
    ## Função criada para retornar um json do modelo nas requisições
    def json(self):
        return {
            'transacao_id':self.transacao_id,
            'valor':float(self.valor),
            'tipo':self.tipo,
            'data':str(self.data),
            'descricao:':self.descricao,
            'usuario':{'id': self.usuario_id, 'nome':str(self.usuario.nome)},
            'conta':self.conta_id,
            'categoria':self.categorias.nome_categoria
        }
        
    ## Procurar modelo pelo id
    @classmethod 
    def findById(cls,id):
        return cls.query.get(id)
    
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