from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
from flask import request, jsonify, abort

# local import
from instance.config import app_config

# initialize sql-alchemy
db = SQLAlchemy()


def create_app(config_name):
    from app.models import UnidadeExploracao

    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    @app.route('/UnidadeExploracao/', methods=['POST', 'GET'])
    def unidadesExploracao():
        if request.method == "POST":
            nrUnidadeExploracao = str(request.data.get('nrUnidadeExploracao', ''))
            if nrUnidadeExploracao:
                unidExp = UnidadeExploracao(nrUnidadeExploracao=nrUnidadeExploracao)
                unidExp.save()
                response = jsonify({
                    'idUnidadeExploracao': unidExp.idUnidadeExploracao,
                    'nrUnidadeExploracao': unidExp.nrUnidadeExploracao,
                    'qtCapacidadeAlojamento': unidExp.qtCapacidadeAlojamento,
                    'csTipoUnidadeExploracao': unidExp.csTipoUnidadeExploracao,
                    'stAtiva': unidExp.stAtiva,
                    'csTipoAnimal': unidExp.csTipoAnimal,
                    'cdEstabelecimento': unidExp.cdEstabelecimento,
                    'created_at': unidExp.created_at,
                    'updated_at': unidExp.updated_at
                })
                response.status_code = 201
                return response
        else:
            # GET
            unidadesExploracao = UnidadeExploracao.get_all()
            results = []

            for unidExp in unidadesExploracao:
                obj = {
                    'idUnidadeExploracao': unidExp.idUnidadeExploracao,
                    'nrUnidadeExploracao': unidExp.nrUnidadeExploracao,
                    'qtCapacidadeAlojamento': unidExp.qtCapacidadeAlojamento,
                    'csTipoUnidadeExploracao': unidExp.csTipoUnidadeExploracao,
                    'stAtiva': unidExp.stAtiva,
                    'csTipoAnimal': unidExp.csTipoAnimal,
                    'cdEstabelecimento': unidExp.cdEstabelecimento,
                    'created_at': unidExp.created_at,
                    'updated_at': unidExp.updated_at
                }
                results.append(obj)
            response = jsonify(results)
            response.status_code = 200
            return response

    return app