from sqlAlchemy import banco
from sqlalchemy import Column, Integer, ForeignKey, Float, Double, String, DateTime, Date, Text, func
from sqlalchemy.orm import relationship

class Meta(banco.Model):
    __tablename__ = 'meta'
    
    meta_id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey('usuario.usuario_id'), nullable=False)
    nome_meta = Column(String(150), nullable=False)
    valor_meta = Column(Float, nullable=False)
    data_limite = Column(Date, nullable=False)
    valor_acumulado = Column(Float)
    usuario = relationship("Usuario", back_populates="metas")
    
    
    def __init__(self,usuario_id=None,nome_meta=None,valor_meta=None,data_limite=None,valor_acumulado=None):
        self.usuario_id = usuario_id
        self.nome_meta = nome_meta
        self.valor_meta = valor_meta
        self.data_limite = data_limite
        valor_acumulado = valor_acumulado
    
    ## Função criada para retornar um json do modelo nas requisições
    def json(self):
        return {
            'meta_id':self.meta_id,
            'nome_meta':self.nome_meta,
            'valor_meta':float(self.valor_meta),
            'data_limite':str(self.data_limite),
            'valor_acumulado':float(self.valor_acumulado),
            'usuario':self.usuario.json()
        }

    