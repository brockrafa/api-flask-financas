from flask_restful import Resource
from src.service.MetaService import *
from flask import request
from marshmallow import Schema, fields, ValidationError, EXCLUDE


class MetaSchema(Schema):
    usuario_id = fields.Integer(required=True, error_messages={'invalid':'O formato do campo usuario_id deve ser um inteiro','required':"O campo usuario_id é obrigatório"})
    nome_meta = fields.String(required=True, error_messages={'required':"O campo nome_meta é obrigatório"})
    valor_meta = fields.Float(required=True, error_messages={'required':"O campo valor_meta é obrigatório"})
    valor_acumulado = fields.Float(required=True, error_messages={'required':"O campo valor_acumulado é obrigatório"})
    data_limite = fields.Date(required=True, error_messages={'invalid':'O formato de data é: yyyy-mm-dd','required':"O campo data_limite é obrigatório"})
    
    class Meta:
        unknown = EXCLUDE  # Ignora campos não definidos no esquema

class MetaListController(Resource):
    
    def get(self):
        usuarioId = None
        if request.headers.get('Authorization'):
            usuarioId = request.headers.get('Authorization')
        metas = getMetasByUsuario(usuarioId)
        return metas
    
    def post(self):
        try:
            MetaSchema().load(request.form)
            dados = dict(request.form.items())
            meta = addMeta(dados)
            return meta.json()
        except ValidationError as err:
            return {'errors': err.messages}, 400
        except Exception as err:
            return {'errors': {"erro":[str(err)]}}, 400
    
class MetaItemController(Resource):
    def get(self, meta_id):
        meta = getMetaById(meta_id)
        if meta:
            return meta.json()
        return {"mensagem":f"Meta {meta_id} não existe!"},404
    
    def put(self, meta_id):
        try:
            MetaSchema().load(request.form)
            dados = dict(request.form.items())
            meta = updateMeta(meta_id,dados)
            return {"mensagem":"Meta atualizada com sucesso",'meta':meta.json()}
        except Exception as err:
            return {'errors': {"erro":[str(err)]}}, 400
    
    def delete(self, meta_id):
        try: 
            return deleteMeta(meta_id)
        except Exception as err:
            return {'errors': {"erro":[str(err)]}}, 400