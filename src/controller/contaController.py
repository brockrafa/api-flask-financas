from flask_restful import Resource
from src.service.ContaService import *
from flask import request
from marshmallow import Schema, fields, ValidationError, EXCLUDE

class ContaSchema(Schema):
    usuario_id = fields.Integer(required=True, error_messages={'invalid':"O formato do campo enviado não é valido",'required':"O campo usuario_id é obrigatório"})
    nome_conta = fields.String(required=True, error_messages={'required':"O campo nome_conta é obrigatório"})
    saldo_inicial = fields.String(required=True, error_messages={'required':"O campo saldo_inicial é obrigatório"})
    
    class Meta:
        unknown = EXCLUDE  # Ignora campos não definidos no esquema

class ContaListController(Resource):
    
    def get(self):
        usuarioId = None
        if request.headers.get('Authorization'):
            usuarioId = request.headers.get('Authorization')
        contas = getContasByUsuario(usuarioId)
        return contas
    
    def post(self):
        try:
            ContaSchema().load(request.form)
            dados = dict(request.form.items())
            conta = addConta(dados['usuario_id'],dados['nome_conta'],dados['saldo_inicial'])
            return conta.json()
        except ValidationError as err:
            return {'errors': err.messages}, 400
        except Exception as err:
            return {'errors': {"erro":[str(err)]}}, 400
       
    
class ContaItemController(Resource):
    
    def get(self, conta_id):
        conta = getContaById(conta_id)
        if conta:
            return conta.json()
        return {"mensagem":f"Conta {conta_id} não existe!"},404
    
    def put(self, conta_id):
        try:
            ContaSchema().load(request.form)
            dados = request.form
            conta = updateCategoria(conta_id,dados)
            return {"mensagem":"Conta atualizada com sucesso",'conta':conta.json()}
        except Exception as err:
            return {'errors': {"erro":[str(err)]}}, 400
    
    def delete(self, conta_id):
        try: 
            return deleteConta(conta_id)
        except Exception as err:
            return {'errors': {"erro":[str(err)]}}, 400
        
        
