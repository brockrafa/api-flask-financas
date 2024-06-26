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
            'data_criacao':str(self.data_criacao),
            'senha':self.senha
        }
        
    ## Salvar modelo no banco
    def save(self):
        banco.session.add(self)
        banco.session.commit()
    
    ## Obter todos os registros do modelo   
    @classmethod 
    def getAll(cls):
        return cls.query.all()
    
    ## Procurar modelo pelo id
    @classmethod 
    def findById(cls,id):
        return cls.query.get(id)
    
    ## Atualizar modelo
    def update(self, args):
        for chave, valor in args.form.items():
            setattr(self, chave, valor)
       
        banco.session.add(self)
        banco.session.commit()
      
    ## Deletar modelo    
    def delete(self):
        banco.session.delete(self)
        banco.session.commit()
        
    @classmethod
    def findUsuarioLogin(cls,dados):
        try:
            email = dados['email']
            senha = dados['senha']

            # Consulta para encontrar o usuário pelo email
            usuario = cls.query.filter_by(email=email).first()

            if usuario and usuario.senha == senha:
                return usuario
            else:
                return None

        except SQLAlchemyError as e:
            print(f'Erro ao buscar usuário: {str(e)}')
            return None