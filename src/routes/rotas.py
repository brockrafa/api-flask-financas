
from src.controller.usuarioController import UsuarioListController,UsuarioItemController
from src.controller.contaController import ContaListController, ContaItemController
from src.controller.categoriaController import CategoriaListController, CategoriaItemController
from src.controller.metaController import MetaListController, MetaItemController
from src.controller.transacaoController import TransacaoListController, TransacaoItemController


def initialize_endpoints(api,app):
   api.add_resource(UsuarioListController, "/usuario")
   api.add_resource(UsuarioItemController, "/usuario/<int:usuario_id>")
   api.add_resource(ContaListController, "/conta")
   api.add_resource(ContaItemController, "/conta/<int:conta_id>")
   api.add_resource(CategoriaListController, "/categoria")
   api.add_resource(CategoriaItemController, "/categoria/<int:categoria_id>")
   api.add_resource(MetaListController, "/meta")
   api.add_resource(MetaItemController, "/meta/<int:meta_id>")
   api.add_resource(TransacaoListController, "/transacao")
   api.add_resource(TransacaoItemController, "/transacao/<int:transacao_id>") 
   #Rota personalizada
   @app.route('/usuario/login', methods=['POST'])
   def loginUsuario():
      return UsuarioItemController().login()