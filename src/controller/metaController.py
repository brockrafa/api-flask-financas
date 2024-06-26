from flask_restful import Resource
from src.model.meta import Meta
from src.model.usuario import Usuario
from flask import request
from flask import jsonify
from marshmallow import Schema, fields, ValidationError, validate, EXCLUDE


class MetaSchema(Schema):
    usuario_id = fields.Integer(required=True, error_messages={'invalid':'O formato do campo usuario_id deve ser um inteiro','required':"O campo usuario_id é obrigatório"})
    nome_meta = fields.String(required=True, error_messages={'required':"O campo nome_meta é obrigatório"})
    valor_meta = fields.Float(required=True, error_messages={'required':"O campo valor_meta é obrigatório"})
    valor_acumulado = fields.Float(required=False, error_messages={'required':"O campo valor_acumulado é obrigatório"})
    data_limite = fields.Date(required=True, error_messages={'invalid':'O formato de data é: yyyy-mm-dd','required':"O campo data_limite é obrigatório"})
    
    class Meta:
        unknown = EXCLUDE  # Ignora campos não definidos no esquema

class MetaListController(Resource):
    
    def get(self):
        if not request.headers.get('Authorization'):
            return {"mensagem":"É necessário enviar o ID de usuario no header Authorization"}
        usuarioId = request.headers.get('Authorization')
        
        metas = Meta.getAll(usuarioId)
        resposta = []
        for meta in metas:
            resposta.append(meta.json())
        return resposta
    
    def post(self):
        try:
            MetaSchema().load(request.form)
            if not Usuario.findById(request.form.get('usuario_id')):
                return {'mensagem':"Usuário não existe. Confira os campos enviados"}
            meta = Meta()
            meta.usuario_id = request.form.get('usuario_id')
            meta.nome_meta = request.form.get('nome_meta')
            meta.valor_meta = request.form.get('valor_meta')
            meta.data_limite = request.form.get('data_limite')
            meta.valor_acumulado = 0
            meta.save()
            return meta.json()
        except ValidationError as err:
            return {'errors': err.messages}, 400
    
class MetaItemController(Resource):
    def get(self, meta_id):
        meta = Meta.findById(meta_id)
        if meta:
            return meta.json()
        return {"msg":f"Meta: {meta_id} não existe!"}, 404
    
    def put(self, meta_id):
        if request.form.get('usuario_id') or request.form.get('meta_id'):
             return {"msg":"Não é possível atualizar o usuario_id ou meta_id"}, 401
        meta = Meta.findById(meta_id)
        if meta:
            for chave, valor in request.form.items():
                setattr(meta, chave, valor)
            meta.update()
            return {"msg": f"Meta número: {meta_id} atualizada com sucesso!", "Meta":meta.json()},  200
        
        return {"msg":f"Meta número: {meta} não existe!"}, 404
    
    def delete(self, meta_id):
        meta = Meta.findById(meta_id)
        if meta:
            meta.delete()
            return {"msg": f"Meta: {meta_id} deletada com sucesso!"}, 200
        
        return {"msg":f"Meta: {meta_id} não existe!"}, 404