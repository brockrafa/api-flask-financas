from src.model.usuario import Usuario
from src.model.conta import Conta
from src.repository.UsuarioRepository import *

def addUsuario(nome,email,senha) -> Usuario:
    if not existe_email(email):
        usuario = add_usuario(nome,email,senha)
        return usuario
    else:
        raise Exception("Email informado já cadastrado")
    
def getUsuarios():
    usuarios = get_usuarios()
    response = []
    if usuarios:
        for usuario in usuarios:
            response.append(usuario.json())
        return response
    return usuarios

def getUsuarioById(id):
    return  get_usuario_by_id(id)

def updateUsuario(id,dados):
    nome = dados.get("nome")
    return update_usuario(id,nome)

def deleteUsuario(id):
    conta = Conta.findByUsuarioId(id)
    if conta:
        return {"mensagem":"Usuario não pode ser deletado pois existem contas cadastradas por ele"}
    status = delete_usuario(id)
    
    if status:
        return {"mensagem":"Usuario excluido com sucesso"}
    return {"mensagem":"Nenhum usuario encontrado"}

def loginUsuario(dados):
    if 'email' in dados and 'senha' in  dados:
        email = dados['email']
        senha = dados['senha']
        usuario = autenticar_usuario(email,senha)
        if usuario == None:
            return {'mensagem':"Usuario não encontrado"},404
        return {"mensagem":"Login efetuado com sucesso","usuario":usuario.json()},200
       
    return {"mensagem":"Os campos email e senha são obrigatórios"}
    
    