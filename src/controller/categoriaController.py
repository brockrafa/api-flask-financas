from flask_restful import Resource
from flask import request
from marshmallow import Schema, fields, ValidationError, EXCLUDE
from src.service.CategoriaService import *


class CategoriaSchema(Schema):
    usuario_id = fields.Integer(required=True, error_messages={'invalid':'O formato do campo usuario_id deve ser um inteiro','required':"O campo usuario_id é obrigatório"})
    nome_categoria = fields.String(required=True, error_messages={'required':"O campo nome_categoria é obrigatório"})
    tipo = fields.String(required=True, error_messages={'required':"O campo tipo é obrigatório"})
    
    class Meta:
        unknown = EXCLUDE  # Ignora campos não definidos no esquema
    
class CategoriaListController(Resource):
    
    def get(self):
        usuarioId = None
        if request.headers.get('Authorization'):
            usuarioId = request.headers.get('Authorization')
        categorias = getCategoriasByUsuario(usuarioId)
        return categorias
    
    def post(self):
        try:
            CategoriaSchema().load(request.form)
            dados = dict(request.form.items())
            categoria = add_categoria(dados['usuario_id'],dados['nome_categoria'],dados['tipo'])
            return categoria.json()
        except ValidationError as err:
            return {'errors': err.messages}, 400
        except Exception as err:
            return {'errors': {"erro":[str(err)]}}, 400
    
class CategoriaItemController(Resource):
    def get(self, categoria_id):
        categoria = getCategoriaById(categoria_id)
        if categoria:
            return categoria.json()
        return {"mensagem":f"Categoria {categoria_id} não existe!"},404
    
    def put(self, categoria_id):
        try:
            CategoriaSchema().load(request.form)
            dados = request.form
            categoria = updateCategoria(categoria_id,dados)
            return {"mensagem":"Categoria atualizada com sucesso",'categoria':categoria.json()}
        except Exception as err:
            return {'errors': {"erro":[str(err)]}}, 400
    
    def delete(self, categoria_id):
        try: 
            return deleteCategoria(categoria_id)
        except Exception as err:
            return {'errors': {"erro":[str(err)]}}, 400