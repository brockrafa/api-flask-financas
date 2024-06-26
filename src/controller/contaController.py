from flask_restful import Resource
from src.model.conta import Conta
from flask import request
from flask import jsonify
from marshmallow import Schema, fields, ValidationError, validate, EXCLUDE

class CategoriaSchema(Schema):
    usuario_id = fields.Integer(required=True, error_messages={'invalid':"O formato do campo enviado não é valido",'required':"O campo usuario_id é obrigatório"})
    nome_conta = fields.String(required=True, error_messages={'required':"O campo nome_conta é obrigatório"})
    
    class Meta:
        unknown = EXCLUDE  # Ignora campos não definidos no esquema

class ContaListController(Resource):
    
    def get(self):
        contas = Conta.getAll()
        resposta = []
        for conta in contas:
            resposta.append(conta.json())
        return resposta
    
    def post(self):
        try:
            CategoriaSchema().load(request.form)
            conta = Conta() 
            conta.usuario_id = request.form.get('usuario_id')
            conta.nome_conta = request.form.get('nome_conta')
            conta.saldo_inicial = 0.0
            conta.save()
            return {'msg':'Conta criada com sucesso','conta':conta.json()}
        except ValidationError as err:
            return {'errors': err.messages}, 400
       
    
class ContaItemController(Resource):
    
    def get(self, conta_id):
        conta = Conta.findById(conta_id)
        if conta:
            return conta.json()
        return {"msg":f"Conta número: {conta_id} não existe!"}, 404
    
    def put(self, conta_id):
        if request.form.get('usuario_id') or request.form.get('conta_id'):
             return {"msg":"Não é possível atualizar o usuario_id ou conta_id"}, 401
         
        conta = Conta.findById(conta_id)
       
        if conta:
            for chave, valor in request.form.items():
                setattr(conta, chave, valor)
            conta.update()
            return {"msg": f"Conta número: {conta_id} atualizada com sucesso!", "conta":conta.json()},  200
        
        return {"msg":f"Conta número: {conta_id} não existe!"}, 404
    
    def delete(self, conta_id):
        conta = Conta.findById(conta_id)
        if conta:
            conta.delete()
            return {"msg": f"Conta número: {conta_id} deletada com sucesso!"}, 200
        
        return {"msg":f"Conta número: {conta_id} não existe!"}, 404
        
        
