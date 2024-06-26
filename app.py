from flask import Flask
from flask_restful import Api
from src.routes.rotas import initialize_endpoints

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:123@localhost:5432/db_financas'

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

api = Api(app)

@app.before_request
def criarBanco():
    # banco.drop_all()
    # banco.create_all()
    pass

initialize_endpoints(api,app)

if __name__ == '__main__':
    from sqlAlchemy import banco
    banco.init_app(app)
    app.run(debug=True)