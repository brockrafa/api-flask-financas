from flask_restful import Resource
from src.model.transacao import Transacao
from src.model.usuario import Usuario
from src.model.categoria import Categoria
from src.model.conta import Conta
from flask import request
from marshmallow import Schema, fields, ValidationError, EXCLUDE
from src.service.TransacaoService import *

class TransacaoSchema(Schema):
    usuario_id = fields.Integer(required=True, error_messages={'invalid':"O formato do campo enviado não é valido",'required':"O campo usuario_id é obrigatório"})
    conta_id = fields.Integer(required=True, error_messages={'invalid':"O formato do campo enviado não é valido",'required':"O campo conta_id é obrigatório"})
    categoria_id = fields.Integer(required=True, error_messages={'invalid':"O formato do campo enviado não é valido",'required':"O campo categoria_id é obrigatório"})
    valor = fields.Float(required=True, error_messages={'invalid':"O formato do campo valor enviado não é valido",'required':"O campo valor é obrigatório"})
    tipo = fields.String(required=True, error_messages={'invalid':"O formato do campo enviado não é valido",'required':"O campo tipo é obrigatório"})
    descricao = fields.String(required=True, error_messages={'invalid':"O formato do campo enviado não é valido",'required':"O campo descricao é obrigatório"})
    
    class Meta:
        unknown = EXCLUDE  # Ignora campos não definidos no esquema


class TransacaoListController(Resource):
    
    def get(self):
        usuarioId = None
        if request.headers.get('Authorization'):
            usuarioId = request.headers.get('Authorization')
        transacoes = getTransacoesByUsuario(usuarioId)
        return transacoes
    
    def post(self):
        try:
            TransacaoSchema().load(request.form)
            dados = dict(request.form.items())
            transacao = addTransacao(dados)
            return transacao.json()
        except ValidationError as err:
            return {'errors': err.messages}, 400
        except Exception as err:
            return {'errors': {"erro":[str(err)]}}, 400
    
class TransacaoItemController(Resource):
    def get(self, transacao_id):
        transacao = getTransacaoById(transacao_id)
        if transacao:
            return transacao.json()
        return {"mensagem":f"Transação {transacao_id} não existe!"},404
    
    def put(self, transacao_id):
        try:
            TransacaoSchema().load(request.form)
            dados = dict(request.form.items())
            transacao = updateTransacao(transacao_id,dados)
            return {"mensagem":"Conta atualizada com sucesso",'conta':transacao.json()}
        except Exception as err:
            return {'errors': {"erro":[str(err)]}}, 400

    def delete(self, transacao_id):
        try: 
            return deleteTransacao(transacao_id)
        except Exception as err:
            return {'errors': {"erro":[str(err)]}}, 400
        
