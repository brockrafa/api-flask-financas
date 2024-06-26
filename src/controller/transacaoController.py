from flask_restful import Resource
from src.model.transacao import Transacao
from src.model.usuario import Usuario
from src.model.categoria import Categoria
from src.model.conta import Conta
from flask import request
from flask import jsonify
from marshmallow import Schema, fields, ValidationError, validate, EXCLUDE

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
        transacao = Transacao.getAll()
        
        resposta = []
        for transacao in transacao:
            resposta.append(transacao.json())
        return resposta
    
    def post(self):
        try:
            TransacaoSchema().load(request.form)
            if not Usuario().findById(request.form.get('usuario_id')) :
                return {"mensagem":"O id de usuario informado não existe"},404
            if not Categoria().findById(request.form.get('categoria_id')):
                return {"mensagem":"O id de categoria informado não existe"},404
            if not Conta().findById(request.form.get('conta_id')):
                return {"mensagem":"O id de conta informado não existe"},404
                
            transacao = Transacao()
            transacao.usuario_id = request.form.get('usuario_id')
            transacao.conta_id = request.form.get('conta_id')
            transacao.categoria_id = request.form.get('categoria_id')
            transacao.valor = request.form.get('valor')
            transacao.tipo = request.form.get('tipo')
            transacao.descricao = request.form.get('descricao')
            transacao.save()
            return transacao.json()
        except ValidationError as err:
            return {'errors': err.messages}, 400
    
class TransacaoItemController(Resource):
    def get(self, transacao_id):
        transacao = Transacao.findById(transacao_id)
        if transacao:
            return transacao.json()
        return {"msg":f"Transação: {transacao_id} não existe!"}, 404
    
    def put(self, transacao_id):
        if request.form.get('usuario_id') or request.form.get('transacao_id'):
             return {"msg":"Não é possível atualizar o usuario_id ou transacao_id"}, 401
        transacao = Transacao.findById(transacao_id)
        if transacao:
            for chave, valor in request.form.items():
                setattr(transacao, chave, valor)
            transacao.update()
            return {"msg": f"Transacao: {transacao_id} atualizada com sucesso!", "conta":transacao.json()},  200
        
        return {"msg":f"Transação: {transacao_id} não existe!"}, 404
    
    def delete(self, transacao_id):
        transacao = Transacao.findById(transacao_id)
        if transacao:
            transacao.delete()
            return {"msg": f"Transação: {transacao_id} deletada com sucesso!"}, 200
        
        return {"msg":f"Transação: {transacao_id} não existe!"}, 404
        
        
