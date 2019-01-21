import unittest
import os
import json
from app import create_app, db


class EstabelecimentoTestCase(unittest.TestCase):
    """This class represents the estabelecimento test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.estabelecimento = {
            "nmEstabelecimento": "Granja Santa Clara",
            "nrCodigoOficial": "42-0003256",
            "idPais": 1,
            "idUf": 24,
            "idMunicipio": 2812,
            "nmLocalidade": "Rua Retangular, número 182. Bairro Santa Clara.",
            "nrLatitude": -28.098883,
            "nrLongitude": -28.098883,
            "stAtivo": True,
            "idCliente": 10
        }
        self.produtor1 = {
            "nrDocumento": "083.843.589-07",
            "nmProdutor": "Fernando Paladini",
            "nrTelefone": "(48) 99845-9684",
            "dsEmail": "paladini@1doc.com.br",
            "cdEstabelecimento": 0
        }
        self.produtor2 = {
            "nrDocumento": "281.512.589-07",
            "nmProdutor": "Fernando Paladini Joi",
            "nrTelefone": "(48) 99845-9684",
            "dsEmail": "fnpaladini@gmail.com",
            "cdEstabelecimento": 0
        }
        self.unidExp1 = {
            "nrUnidadeExploracao": 19515,
            "qtCapacidadeAlojamento": 250,
            "csTipoUnidadeExploracao": "UPL",
            "stAtiva": True,
            "csTipoAnimal": "SU",
            "cdEstabelecimento": 0
        }
        self.unidExp2 = {
            "nrUnidadeExploracao": 8591,
            "qtCapacidadeAlojamento": 150,
            "csTipoUnidadeExploracao": "Terminação",
            "stAtiva": True,
            "csTipoAnimal": "AV",
            "cdEstabelecimento": 0
        }

        # binds the app to the current context
        with self.app.app_context():
            # create all tables
            db.create_all()

    def test_estabelecimento_creation(self):
        """Test API can create a estabelecimento (POST request)"""
        res = self.client().post('/Estabelecimento/', data=self.estabelecimento)
        res_json = json.loads(res.data.decode('utf-8').replace("'", "\""))
        self.assertEqual(res.status_code, 201)
        self.assertEqual(self.estabelecimento["nmEstabelecimento"], res_json["nmEstabelecimento"])
        self.assertEqual(self.estabelecimento["nrCodigoOficial"], res_json["nrCodigoOficial"])
        self.assertEqual(self.estabelecimento["idPais"], res_json["idPais"])
        self.assertEqual(self.estabelecimento["idUf"], res_json["idUf"])
        self.assertEqual(self.estabelecimento["idMunicipio"], res_json["idMunicipio"])
        self.assertEqual(self.estabelecimento["nmLocalidade"], res_json["nmLocalidade"])
        self.assertEqual(self.estabelecimento["nrLatitude"], res_json["nrLatitude"])
        self.assertEqual(self.estabelecimento["nrLongitude"], res_json["nrLongitude"])
        self.assertEqual(self.estabelecimento["stAtivo"], res_json["stAtivo"])
        self.assertEqual(self.estabelecimento["idCliente"], res_json["idCliente"])

    def test_api_can_get_all_estabelecimentos(self):
        """Test API can get a estabelecimento (GET request)."""

        # Insert new estabelecimento
        res = self.client().post('/Estabelecimento/', data=self.estabelecimento)
        self.assertEqual(res.status_code, 201)
        
        # Get inserted estabelecimentos
        res = self.client().get('/Estabelecimento/')
        res_json = json.loads(res.data.decode('utf-8').replace("'", "\""))
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(self.estabelecimento["nmEstabelecimento"], res_json[0]["nmEstabelecimento"])
        self.assertEqual(self.estabelecimento["nrCodigoOficial"], res_json[0]["nrCodigoOficial"])
        self.assertEqual(self.estabelecimento["idPais"], res_json[0]["idPais"])
        self.assertEqual(self.estabelecimento["idUf"], res_json[0]["idUf"])
        self.assertEqual(self.estabelecimento["idMunicipio"], res_json[0]["idMunicipio"])
        self.assertEqual(self.estabelecimento["nmLocalidade"], res_json[0]["nmLocalidade"])
        self.assertEqual(self.estabelecimento["nrLatitude"], res_json[0]["nrLatitude"])
        self.assertEqual(self.estabelecimento["nrLongitude"], res_json[0]["nrLongitude"])
        self.assertEqual(self.estabelecimento["stAtivo"], res_json[0]["stAtivo"])
        self.assertEqual(self.estabelecimento["idCliente"], res_json[0]["idCliente"])


    def test_api_can_get_estabelecimento_by_id(self):
        """Test API can get a single estabelecimento by using it's id."""

        # Insert new estabelecimento
        rv = self.client().post('/Estabelecimento/', data=self.estabelecimento)
        self.assertEqual(rv.status_code, 201)

        # Get the estabelecimento recently created.
        res_json = json.loads(rv.data.decode('utf-8').replace("'", "\""))
        result = self.client().get('/Estabelecimento/{}'.format(res_json['idEstabelecimento']))
        
        # Assert that estabelecimento exists and has the same value of the inserted estabelecimento.
        self.assertEqual(result.status_code, 200)
        self.assertEqual(self.estabelecimento["nmEstabelecimento"], res_json["nmEstabelecimento"])
        self.assertEqual(self.estabelecimento["nrCodigoOficial"], res_json["nrCodigoOficial"])
        self.assertEqual(self.estabelecimento["idPais"], res_json["idPais"])
        self.assertEqual(self.estabelecimento["idUf"], res_json["idUf"])
        self.assertEqual(self.estabelecimento["idMunicipio"], res_json["idMunicipio"])
        self.assertEqual(self.estabelecimento["nmLocalidade"], res_json["nmLocalidade"])
        self.assertEqual(self.estabelecimento["nrLatitude"], res_json["nrLatitude"])
        self.assertEqual(self.estabelecimento["nrLongitude"], res_json["nrLongitude"])
        self.assertEqual(self.estabelecimento["stAtivo"], res_json["stAtivo"])
        self.assertEqual(self.estabelecimento["idCliente"], res_json["idCliente"])

    def test_estabelecimento_can_be_edited(self):
        """Test API can edit an existing estabelecimento. (PUT request)"""
        updated_data = {
            "nmEstabelecimento": "Um outro nome qualquer",
            "nrCodigoOficial": "42-0003256",
            "idPais": 1,
            "idUf": 24,
            "idMunicipio": 2812,
            "nmLocalidade": "Rua Retangular, número 182. Bairro Santa Clara.",
            "nrLatitude": -28.098883,
            "nrLongitude": -28.098883,
            "stAtivo": True,
            "idCliente": 10
        }

        # Insert new estabelecimento
        rv = self.client().post('/Estabelecimento/', data=self.estabelecimento)
        self.assertEqual(rv.status_code, 201)

        # Update estabelecimento
        rv = self.client().put('/Estabelecimento/1', data=updated_data)
        self.assertEqual(rv.status_code, 200)

        # Get same estabelecimento and check if the name has changed.
        results = self.client().get('/Estabelecimento/1')
        res_json = json.loads(results.data.decode('utf-8').replace("'", "\""))
        
        self.assertEqual(updated_data["nmEstabelecimento"], res_json["nmEstabelecimento"])
        self.assertEqual(updated_data["nrCodigoOficial"], res_json["nrCodigoOficial"])
        self.assertEqual(updated_data["idPais"], res_json["idPais"])
        self.assertEqual(updated_data["idUf"], res_json["idUf"])
        self.assertEqual(updated_data["idMunicipio"], res_json["idMunicipio"])
        self.assertEqual(updated_data["nmLocalidade"], res_json["nmLocalidade"])
        self.assertEqual(updated_data["nrLatitude"], res_json["nrLatitude"])
        self.assertEqual(updated_data["nrLongitude"], res_json["nrLongitude"])
        self.assertEqual(updated_data["stAtivo"], res_json["stAtivo"])
        self.assertEqual(updated_data["idCliente"], res_json["idCliente"])

    def test_estabelecimento_deletion(self):
        """Test API can delete an existing estabelecimento. (DELETE request)."""
        
        # Create new estabelecimento
        rv = self.client().post('/Estabelecimento/', data=self.estabelecimento)
        self.assertEqual(rv.status_code, 201)

        # Delete estabelecimento created earlier
        res = self.client().delete('/Estabelecimento/1')
        self.assertEqual(res.status_code, 200)

        # Test to see if it exists, should return a 404
        result = self.client().get('/Estabelecimento/1')
        self.assertEqual(result.status_code, 404)

    def test_api_get_produtores_by_estabelecimento_id(self):
        """Get produtores from a given estabelecimento by using it's id."""

        # Insert new estabelecimento
        rv = self.client().post('/Estabelecimento/', data=self.estabelecimento)
        self.assertEqual(rv.status_code, 201)

        # Get the estabelecimento recently created and associate it with the produtor.
        res_json = json.loads(rv.data.decode('utf-8').replace("'", "\""))
        self.produtor1["cdEstabelecimento"] = res_json["idEstabelecimento"]
        self.produtor2["cdEstabelecimento"] = res_json["idEstabelecimento"]

        # Create a new produtor
        res = self.client().post('/Produtor/', data=self.produtor1)
        self.assertEqual(res.status_code, 201)

        # Create a new produtor
        res = self.client().post('/Produtor/', data=self.produtor2)
        self.assertEqual(res.status_code, 201)

        # Check if produtores was correctly associated with Estabelecimento
        result = self.client().get('/Estabelecimento/{}/Produtor'.format(res_json['idEstabelecimento']))
        res_json = json.loads(result.data.decode('utf-8').replace("'", "\""))

        # Assert that produtores exists and has the same value of the inserted estabelecimento.
        self.assertEqual(result.status_code, 200)
        self.assertEqual(2, len(res_json))
        
        # Assert produtor1 data.
        self.assertEqual(self.produtor1["nrDocumento"], res_json[0]["nrDocumento"])
        self.assertEqual(self.produtor1["nmProdutor"], res_json[0]["nmProdutor"])
        self.assertEqual(self.produtor1["nrTelefone"], res_json[0]["nrTelefone"])
        self.assertEqual(self.produtor1["dsEmail"], res_json[0]["dsEmail"])
        self.assertEqual(self.produtor1["cdEstabelecimento"], res_json[0]["cdEstabelecimento"])
        
        # Assert produto2 data.
        self.assertEqual(self.produtor2["nrDocumento"], res_json[1]["nrDocumento"])
        self.assertEqual(self.produtor2["nmProdutor"], res_json[1]["nmProdutor"])
        self.assertEqual(self.produtor2["nrTelefone"], res_json[1]["nrTelefone"])
        self.assertEqual(self.produtor2["dsEmail"], res_json[1]["dsEmail"])
        self.assertEqual(self.produtor2["cdEstabelecimento"], res_json[1]["cdEstabelecimento"])
        

    def test_api_get_unidade_exploracao_by_estabelecimento_id(self):
        """Get UnidadeExploracao from a given estabelecimento by using it's id."""

        # Insert new estabelecimento
        rv = self.client().post('/Estabelecimento/', data=self.estabelecimento)
        self.assertEqual(rv.status_code, 201)

        # Get the estabelecimento recently created and associate it with the produtor.
        res_json = json.loads(rv.data.decode('utf-8').replace("'", "\""))
        self.unidExp1["cdEstabelecimento"] = res_json["idEstabelecimento"]
        self.unidExp2["cdEstabelecimento"] = res_json["idEstabelecimento"]

        # Create a new UnidadeExploracao
        res = self.client().post('/Estabelecimento/{}/unidadeExploracao'.format(res_json["idEstabelecimento"]), data=self.unidExp1)
        self.assertEqual(res.status_code, 201)

        # Create a new UnidadeExploracao
        res = self.client().post('/Estabelecimento/{}/unidadeExploracao'.format(res_json["idEstabelecimento"]), data=self.unidExp2)
        self.assertEqual(res.status_code, 201)

        # Check if UnidadeExploracao was correctly associated with Estabelecimento
        result = self.client().get('/Estabelecimento/{}/UnidadeExploracao'.format(res_json['idEstabelecimento']))
        res_json = json.loads(result.data.decode('utf-8').replace("'", "\""))

        # Assert that UnidadeExploracao exists and has the same value of the inserted estabelecimento.
        self.assertEqual(result.status_code, 200)
        self.assertEqual(2, len(res_json))
        
        # Assert unidExp1 data.
        self.assertEqual(self.unidExp1["nrUnidadeExploracao"], res_json[0]["nrUnidadeExploracao"])
        self.assertEqual(self.unidExp1["qtCapacidadeAlojamento"], res_json[0]["qtCapacidadeAlojamento"])
        self.assertEqual(self.unidExp1["csTipoUnidadeExploracao"], res_json[0]["csTipoUnidadeExploracao"])
        self.assertEqual(self.unidExp1["stAtiva"], res_json[0]["stAtiva"])
        self.assertEqual(self.unidExp1["csTipoAnimal"], res_json[0]["csTipoAnimal"])
        self.assertEqual(self.unidExp1["cdEstabelecimento"], res_json[0]["cdEstabelecimento"])
        
        # Assert unidExp2 data.
        self.assertEqual(self.unidExp2["nrUnidadeExploracao"], res_json[1]["nrUnidadeExploracao"])
        self.assertEqual(self.unidExp2["qtCapacidadeAlojamento"], res_json[1]["qtCapacidadeAlojamento"])
        self.assertEqual(self.unidExp2["csTipoUnidadeExploracao"], res_json[1]["csTipoUnidadeExploracao"])
        self.assertEqual(self.unidExp2["stAtiva"], res_json[1]["stAtiva"])
        self.assertEqual(self.unidExp2["csTipoAnimal"], res_json[1]["csTipoAnimal"])
        self.assertEqual(self.unidExp2["cdEstabelecimento"], res_json[1]["cdEstabelecimento"])
       
    def test_api_post_produtor_by_estabelecimento_id(self):
        """Create a new produtor associated with a specific estabelecimento."""

        # Insert new estabelecimento
        rv = self.client().post('/Estabelecimento/', data=self.estabelecimento)
        self.assertEqual(rv.status_code, 201)

        # Get the estabelecimento recently created and associate it with the produtor.
        res_json = json.loads(rv.data.decode('utf-8').replace("'", "\""))
        self.produtor1["cdEstabelecimento"] = res_json["idEstabelecimento"]

        # Create a new produtor associated with the Estabelecimento
        res = self.client().post('/Estabelecimento/{}/produtor'.format(res_json["idEstabelecimento"]), data=self.produtor1)
        self.assertEqual(res.status_code, 201)

        # Check if the produtor was correctly associated with Estabelecimento
        result = self.client().get('/Estabelecimento/{}/Produtor'.format(res_json['idEstabelecimento']))
        res_json = json.loads(result.data.decode('utf-8').replace("'", "\""))

        # Assert that produtor exists and is associated with Estabelecimento.
        self.assertEqual(result.status_code, 200)
        self.assertEqual(1, len(res_json))
        
        # Assert produtor1 data.
        self.assertEqual(self.produtor1["nrDocumento"], res_json[0]["nrDocumento"])
        self.assertEqual(self.produtor1["nmProdutor"], res_json[0]["nmProdutor"])
        self.assertEqual(self.produtor1["nrTelefone"], res_json[0]["nrTelefone"])
        self.assertEqual(self.produtor1["dsEmail"], res_json[0]["dsEmail"])
        self.assertEqual(self.produtor1["cdEstabelecimento"], res_json[0]["cdEstabelecimento"])
    
    def test_api_post_unidade_exploracao_by_estabelecimento_id(self):
        """Create a new UnidadeExploracao associated with a specific estabelecimento."""

        # Insert new estabelecimento
        rv = self.client().post('/Estabelecimento/', data=self.estabelecimento)
        self.assertEqual(rv.status_code, 201)

        # Get the estabelecimento recently created and associate it with the UnidadeExploracao.
        res_json = json.loads(rv.data.decode('utf-8').replace("'", "\""))
        self.unidExp1["cdEstabelecimento"] = res_json["idEstabelecimento"]

        # Create a new unidExp associated with the Estabelecimento
        res = self.client().post('/Estabelecimento/{}/unidadeExploracao'.format(res_json["idEstabelecimento"]), data=self.unidExp1)
        self.assertEqual(res.status_code, 201)

        # Check if the unidExp was correctly associated with Estabelecimento
        result = self.client().get('/Estabelecimento/{}/UnidadeExploracao'.format(res_json['idEstabelecimento']))
        res_json = json.loads(result.data.decode('utf-8').replace("'", "\""))

        # Assert that unidExp exists and is associated with Estabelecimento.
        self.assertEqual(result.status_code, 200)
        self.assertEqual(1, len(res_json))
        
        # Assert unidExp data.
        self.assertEqual(self.unidExp1["nrUnidadeExploracao"], res_json[0]["nrUnidadeExploracao"])
        self.assertEqual(self.unidExp1["qtCapacidadeAlojamento"], res_json[0]["qtCapacidadeAlojamento"])
        self.assertEqual(self.unidExp1["csTipoUnidadeExploracao"], res_json[0]["csTipoUnidadeExploracao"])
        self.assertEqual(self.unidExp1["stAtiva"], res_json[0]["stAtiva"])
        self.assertEqual(self.unidExp1["csTipoAnimal"], res_json[0]["csTipoAnimal"])
        self.assertEqual(self.unidExp1["cdEstabelecimento"], res_json[0]["cdEstabelecimento"])
        

    def test_api_delete_produtor_by_estabelecimento_and_produtor_id(self):
        """Create a new produtor associated with a specific estabelecimento."""

        # Insert new estabelecimento
        rv = self.client().post('/Estabelecimento/', data=self.estabelecimento)
        self.assertEqual(rv.status_code, 201)

        # Get the estabelecimento recently created and associate it with the produtor.
        res_json = json.loads(rv.data.decode('utf-8').replace("'", "\""))
        self.produtor1["cdEstabelecimento"] = res_json["idEstabelecimento"]

        # Create a new produtor associated with the Estabelecimento
        res = self.client().post('/Estabelecimento/{}/produtor'.format(res_json["idEstabelecimento"]), data=self.produtor1)
        res_json = json.loads(res.data.decode('utf-8').replace("'", "\""))
        self.assertEqual(res.status_code, 201)

        # Delete the produtor from the database
        result = self.client().delete('/Estabelecimento/{}/produtor/{}'.format(self.produtor1["cdEstabelecimento"], res_json['idProdutor']))

        # Test to see if it exists, should return a 404
        result = self.client().get('/Produtor/{}'.format(res_json["idProdutor"]))
        self.assertEqual(result.status_code, 404)
        

    def tearDown(self):
        """teardown all initialized variables."""
        with self.app.app_context():
            # drop all tables
            db.session.remove()
            db.drop_all()




# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()