from flask_restful import Resource
from src.model.usuario import Usuario
from src.repository.UsuarioRepository import *
from src.service.UsuarioService import *
from src.model.conta import Conta
from flask import request
from flask import jsonify
from marshmallow import Schema, fields, ValidationError, validate, EXCLUDE

class UserSchema(Schema):
    nome = fields.String(required=True, error_messages={'required':"O campo nome é obrigatório"})
    email = fields.Email(required=True, error_messages={'invalid': 'Email inválido','required':"O campo email é obrigatório"})
    senha = fields.String(required=True,error_messages={'required':"O campo senha é obrigatório"}, validate=[
        validate.Length(min=8, error='A senha deve ter no mínimo 8 caracteres'),
        validate.Regexp(
            regex='^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$',
            error='A senha deve conter pelo menos uma letra maiúscula, uma letra minúscula, um número e um caractere especial'
        )
    ])
    
    class Meta:
        unknown = EXCLUDE  # Ignora campos não definidos no esquema
    

class UsuarioListController(Resource):
    
    def get(self):
       usuarios = getUsuarios()
       if not usuarios:
           return {"mensagem":"Nenhum usuario encontrado"}
       return usuarios
 
    def post(self):
        try:
            UserSchema().load(request.form)
            usuario = addUsuario(request.form.get("nome"),request.form.get("email"),request.form.get("senha"))
            return {'mensagem':'Usuario criado com sucesso','usuario':usuario.json()}
        except ValidationError as err:
            return {'errors': err.messages}, 400
        except Exception as err:
            return {'errors': {"erro":[str(err)]}}, 400
        
class UsuarioItemController(Resource):
    def get(self,usuario_id):
        usuario = getUsuarioById(usuario_id)
        if usuario:
            return usuario.json()
        return jsonify({'mensagem':'Nenhum usuário encontrado com o ID informado'})
    
    def put(self,usuario_id):
        dados = request.form
        usuario = updateUsuario(usuario_id,dados)
        if usuario:
            return {"mensagem":"Usuario atualizado com sucesso",'user':usuario.json()}
        return jsonify({'mensagem':'Nenhum usuario encontrado com o ID informado'})
    
    def delete(self,usuario_id):
        return deleteUsuario(usuario_id)
    
    def login(self):
        dados = dict(request.form.items())
        usuario = loginUsuario(dados)
        

        return usuario

        

    

    
        