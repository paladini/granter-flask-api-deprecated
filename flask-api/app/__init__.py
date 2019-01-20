from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
from flask import request, jsonify, abort

# local import
from instance.config import app_config

# initialize sql-alchemy
db = SQLAlchemy()

def create_app(config_name):
    from app.models import UnidadeExploracao
    from app.models import Estabelecimento
    from app.models import Produtor

    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    #
    # ESTABELECIMENTOS
    #
    @app.route('/Estabelecimento/', methods=['POST', 'GET'])
    def estabelecimentos():
        if request.method == "POST":

            # Get all the parameters for creating an Estabelecimento
            params = Estabelecimento.get_params(request)
            # nmEstabelecimento = str(request.data.get('nmEstabelecimento'))
            # nrCodigoOficial = str(request.data.get('nrCodigoOficial'))
            # idPais = request.data.get('idPais')
            # idUf = request.data.get('idUf')
            # idMunicipio = request.data.get('idMunicipio')
            # nmLocalidade = str(request.data.get('nmLocalidade'))
            # nrLatitude = request.data.get('nrLatitude')
            # nrLongitude = request.data.get('nrLongitude')
            # stAtivo = bool(request.data.get('stAtivo'))
            # idCliente = request.data.get('idCliente')

            if params:
                estab = Estabelecimento(
                    nmEstabelecimento=params["nmEstabelecimento"],
                    nrCodigoOficial=params["nrCodigoOficial"],
                    idPais=params["idPais"],
                    idUf=params["idUf"],
                    idMunicipio=params["idMunicipio"],
                    nmLocalidade=params["nmLocalidade"],
                    nrLatitude=params["nrLatitude"],
                    nrLongitude=params["nrLongitude"],
                    stAtivo=params["stAtivo"],
                    idCliente=params["idCliente"]
                )
                estab.save()

                response = jsonify({
                    'idEstabelecimento': estab.idEstabelecimento,
                    'nmEstabelecimento': estab.nmEstabelecimento,
                    'nrCodigoOficial': estab.nrCodigoOficial,
                    'idPais': estab.idPais,
                    'idUf': estab.idUf,
                    'idMunicipio': estab.idMunicipio,
                    'nmLocalidade': estab.nmLocalidade,
                    'nrLatitude': estab.nrLatitude,
                    'nrLongitude': estab.nrLongitude,
                    'stAtivo': estab.stAtivo,
                    'idCliente': estab.idCliente
                })
                response.status_code = 201
                return response
            else:
                print(request.data)    
        else:

            # GET
            estabelecimentos = Estabelecimento.get_all()
            results = []

            for estab in estabelecimentos:
                obj = {
                    'idEstabelecimento': estab.idEstabelecimento,
                    'nmEstabelecimento': estab.nmEstabelecimento,
                    'nrCodigoOficial': estab.nrCodigoOficial,
                    'idPais': estab.idPais,
                    'idUf': estab.idUf,
                    'idMunicipio': estab.idMunicipio,
                    'nmLocalidade': estab.nmLocalidade,
                    'nrLatitude': estab.nrLatitude,
                    'nrLongitude': estab.nrLongitude,
                    'stAtivo': estab.stAtivo,
                    'idCliente': estab.idCliente
                }
                results.append(obj)
            response = jsonify(results)
            response.status_code = 200
            return response

    @app.route('/Estabelecimento/<int:idEstabelecimento>', methods=['GET', 'PUT', 'DELETE'])
    def estabelecimento_manipulation(idEstabelecimento, **kwargs):
     
        # Retrieve an estabelecimento using it's ID. 
        estab = Estabelecimento.query.filter_by(idEstabelecimento=idEstabelecimento).first()
        if not estab:
            abort(404) # Raise an HTTPException with a 404 not found status code

        # Delete an estabelecimento
        if request.method == 'DELETE':
            estab.delete()
            return ({
                "message": "Estabelecimento {} deleted successfully".format(estab.idEstabelecimento) 
            }, 200)

        # Update an estabelecimento
        elif request.method == 'PUT':

            # Get all params and check if a new value was given in the request
            params = Estabelecimento.get_params(request)

            # if params["nmEstabelecimento"].strip():
            if "nmEstabelecimento" in params:
                estab.nmEstabelecimento = params["nmEstabelecimento"]

            # if params["nrCodigoOficial"].strip():
            if "nrCodigoOficial" in params:
                estab.nrCodigoOficial = params["nrCodigoOficial"]

            # if params["idPais"]:
            if "idPais" in params:
                estab.idPais = params["idPais"]

            # if params["idUf"]:
            if "idUf" in params:
                estab.idUf = params["idUf"]

            # if params["idMunicipio"]:
            if "idMunicipio" in params:
                estab.idMunicipio = params["idMunicipio"]
            
            # if params["nmLocalidade"].strip():
            if "nmLocalidade" in params:
                estab.nmLocalidade = params["nmLocalidade"]
            
            # if params["nrLatitude"]:
            if "nrLatitude" in params:
                estab.nrLatitude = params["nrLatitude"]

            # if params["nrLongitude"]:
            if "nrLongitude" in params:
                estab.nrLongitude = params["nrLongitude"]

            # if params["stAtivo"]:
            if "stAtivo" in params:
                estab.stAtivo = params["stAtivo"]

            # if params["idCliente"]:
            if "idCliente" in params:
                estab.idCliente = params["idCliente"]

            estab.save()
            response = jsonify({
                'idEstabelecimento': estab.idEstabelecimento,
                'nmEstabelecimento': estab.nmEstabelecimento,
                'nrCodigoOficial': estab.nrCodigoOficial,
                'idPais': estab.idPais,
                'idUf': estab.idUf,
                'idMunicipio': estab.idMunicipio,
                'nmLocalidade': estab.nmLocalidade,
                'nrLatitude': estab.nrLatitude,
                'nrLongitude': estab.nrLongitude,
                'stAtivo': estab.stAtivo,
                'idCliente': estab.idCliente
            })
            response.status_code = 200
            return response
        else:
            # GET - Return an estabelecimento
            response = jsonify({
                'idEstabelecimento': estab.idEstabelecimento,
                'nmEstabelecimento': estab.nmEstabelecimento,
                'nrCodigoOficial': estab.nrCodigoOficial,
                'idPais': estab.idPais,
                'idUf': estab.idUf,
                'idMunicipio': estab.idMunicipio,
                'nmLocalidade': estab.nmLocalidade,
                'nrLatitude': estab.nrLatitude,
                'nrLongitude': estab.nrLongitude,
                'stAtivo': estab.stAtivo,
                'idCliente': estab.idCliente
            })
            response.status_code = 200
            return response

    #
    # PRODUTORES
    #
    @app.route('/Produtor/', methods=['POST', 'GET'])
    def produtores():
        if request.method == "POST":

            # Get all the parameters for creating a Produtor
            params = Produtor.get_params(request)

            if params:
                produt = Produtor(
                    nrDocumento=params["nrDocumento"],
                    nmProdutor=params["nmProdutor"],
                    nrTelefone=params["nrTelefone"],
                    dsEmail=params["dsEmail"],
                    cdEstabelecimento=params["cdEstabelecimento"]
                )
                produt.save()

                response = jsonify({
                    'idProdutor': produt.idProdutor,
                    'nrDocumento': produt.nrDocumento,
                    'nmProdutor': produt.nmProdutor,
                    'nrTelefone': produt.nrTelefone,
                    'dsEmail': produt.dsEmail,
                    'cdEstabelecimento': produt.cdEstabelecimento
                })
                response.status_code = 201
                return response
            else:
                print(request.data)    
        else:

            # GET
            produtores = Produtor.get_all()
            results = []

            for produt in produtores:
                obj = {
                    'idProdutor': produt.idProdutor,
                    'nrDocumento': produt.nrDocumento,
                    'nmProdutor': produt.nmProdutor,
                    'nrTelefone': produt.nrTelefone,
                    'dsEmail': produt.dsEmail,
                    'cdEstabelecimento': produt.cdEstabelecimento
                }
                results.append(obj)
            response = jsonify(results)
            response.status_code = 200
            return response

    @app.route('/Produtor/<int:idProdutor>', methods=['GET', 'PUT', 'DELETE'])
    def produtores_manipulation(idProdutor, **kwargs):
     
        # Retrieve a produtor using it's ID. 
        produt = Produtor.query.filter_by(idProdutor=idProdutor).first()
        if not produt:
            abort(404) # Raise an HTTPException with a 404 not found status code

        # Delete a produtor
        if request.method == 'DELETE':
            produt.delete()
            return ({
                "message": "Produtor {} deleted successfully".format(produt.idProdutor) 
            }, 200)

        # Update a produtor
        elif request.method == 'PUT':

            # Get all params and check if a new value was given in the request
            params = Produtor.get_params(request)

            if "nrDocumento" in params:
                produt.nrDocumento = params["nrDocumento"]

            if "nmProdutor" in params:
                produt.nmProdutor = params["nmProdutor"]

            if "nrTelefone" in params:
                produt.nrTelefone = params["nrTelefone"]

            if "dsEmail" in params:
                produt.dsEmail = params["dsEmail"]

            if "cdEstabelecimento" in params:
                produt.cdEstabelecimento = params["cdEstabelecimento"]

            produt.save()
            response = jsonify({
                'idProdutor': produt.idProdutor,
                'nrDocumento': produt.nrDocumento,
                'nmProdutor': produt.nmProdutor,
                'nrTelefone': produt.nrTelefone,
                'dsEmail': produt.dsEmail,
                'cdEstabelecimento': produt.cdEstabelecimento
            })
            response.status_code = 200
            return response
        else:
            # GET - Return a produtor
            response = jsonify({
                'idProdutor': produt.idProdutor,
                'nrDocumento': produt.nrDocumento,
                'nmProdutor': produt.nmProdutor,
                'nrTelefone': produt.nrTelefone,
                'dsEmail': produt.dsEmail,
                'cdEstabelecimento': produt.cdEstabelecimento
            })
            response.status_code = 200
            return response

    #
    # UNIDADES DE EXPLORAÇÃO
    #
    @app.route('/UnidadeExploracao/<int:idUnidadeExploracao>', methods=['GET'])
    def unidadeExploracao_manipulation(idUnidadeExploracao, **kwargs):
        
        # Retrieve an UnidadeExploracao using it's ID
        unidExp = UnidadeExploracao.query.filter_by(idUnidadeExploracao=idUnidadeExploracao).first()
        if not unidExp:
            abort(404) # Raise an HTTPException with a 404 not found status code

        if request.method == 'GET':
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
            response.status_code = 200
            return response
        else:
            response = jsonify({
                "error": "Invalid method"
            })
            response.status_code = 404
            return response

    return app