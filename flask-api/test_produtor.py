import unittest
import os
import json
from app import create_app, db


class ProdutorTestCase(unittest.TestCase):
    """This class represents the produtor test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.produtor = {
            "nrDocumento": "083.843.589-07",
            "nmProdutor": "Fernando Paladini",
            "nrTelefone": "(48) 99845-9684",
            "dsEmail": "paladini@1doc.com.br",
            "cdEstabelecimento": 0
        }
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

        # binds the app to the current context
        with self.app.app_context():
            # create all tables
            db.create_all()

    def test_produtor_creation(self):
        """Test API can create a produtor (POST request)"""

        # Create a new estabelecimento
        estab = self.client().post('/Estabelecimento/', data=self.estabelecimento)
        estab_json = json.loads(estab.data.decode('utf-8').replace("'", "\""))
        self.assertEqual(estab.status_code, 201)

        # Assign estabelecimento to produtor
        self.produtor["cdEstabelecimento"] = estab_json["idEstabelecimento"]

        # Create a new produtor
        res = self.client().post('/Produtor/', data=self.produtor)
        res_json = json.loads(res.data.decode('utf-8').replace("'", "\""))
        self.assertEqual(res.status_code, 201)
        self.assertEqual(self.produtor["nmProdutor"], res_json["nmProdutor"])
        self.assertEqual(self.produtor["nrDocumento"], res_json["nrDocumento"])
        self.assertEqual(self.produtor["nrTelefone"], res_json["nrTelefone"])
        self.assertEqual(self.produtor["dsEmail"], res_json["dsEmail"])
        self.assertEqual(self.produtor["cdEstabelecimento"], res_json["cdEstabelecimento"])

    def test_api_can_get_all_produtores(self):
        """Test API can get a produtor (GET request)."""

        # Create a new estabelecimento
        estab = self.client().post('/Estabelecimento/', data=self.estabelecimento)
        estab_json = json.loads(estab.data.decode('utf-8').replace("'", "\""))
        self.assertEqual(estab.status_code, 201)

        # Assign estabelecimento to produtor
        self.produtor["cdEstabelecimento"] = estab_json["idEstabelecimento"]

        # Insert new produtor
        res = self.client().post('/Produtor/', data=self.produtor)
        self.assertEqual(res.status_code, 201)
        
        # Get inserted produtor
        res = self.client().get('/Produtor/')
        res_json = json.loads(res.data.decode('utf-8').replace("'", "\""))
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(self.produtor["nmProdutor"], res_json[0]["nmProdutor"])
        self.assertEqual(self.produtor["nrDocumento"], res_json[0]["nrDocumento"])
        self.assertEqual(self.produtor["nrTelefone"], res_json[0]["nrTelefone"])
        self.assertEqual(self.produtor["dsEmail"], res_json[0]["dsEmail"])
        self.assertEqual(self.produtor["cdEstabelecimento"], res_json[0]["cdEstabelecimento"])


    def test_api_can_get_produtor_by_id(self):
        """Test API can get a single produtor by using it's id."""

        # Create a new estabelecimento
        estab = self.client().post('/Estabelecimento/', data=self.estabelecimento)
        estab_json = json.loads(estab.data.decode('utf-8').replace("'", "\""))
        self.assertEqual(estab.status_code, 201)

        # Assign estabelecimento to produtor
        self.produtor["cdEstabelecimento"] = estab_json["idEstabelecimento"]

        # Insert new produtor
        rv = self.client().post('/Produtor/', data=self.produtor)
        self.assertEqual(rv.status_code, 201)

        # Get the produtor recently created.
        res_json = json.loads(rv.data.decode('utf-8').replace("'", "\""))
        result = self.client().get('/Produtor/{}'.format(res_json['idProdutor']))
        
        # Assert that produtor exists and has the same value of the inserted produtor.
        res_json = json.loads(result.data.decode('utf-8').replace("'", "\""))
        self.assertEqual(result.status_code, 200)
        self.assertEqual(self.produtor["nmProdutor"], res_json["nmProdutor"])
        self.assertEqual(self.produtor["nrDocumento"], res_json["nrDocumento"])
        self.assertEqual(self.produtor["nrTelefone"], res_json["nrTelefone"])
        self.assertEqual(self.produtor["dsEmail"], res_json["dsEmail"])
        self.assertEqual(self.produtor["cdEstabelecimento"], res_json["cdEstabelecimento"])


    def test_produtor_can_be_edited(self):
        """Test API can edit an existing produtor. (PUT request)"""
        updated_data = {
            "nrDocumento": "072.789.102-10",
            "nmProdutor": "Fernando Paladini Joi",
            "nrTelefone": "(48) 99845-9684",
            "dsEmail": "fnpaladini@gmail.com",
            "cdEstabelecimento": 2
        }

        # Create a new estabelecimento
        estab = self.client().post('/Estabelecimento/', data=self.estabelecimento)
        estab_json = json.loads(estab.data.decode('utf-8').replace("'", "\""))
        self.assertEqual(estab.status_code, 201)

        # Assign estabelecimento to produtor
        self.produtor["cdEstabelecimento"] = estab_json["idEstabelecimento"]
        updated_data["cdEstabelecimento"] = estab_json["idEstabelecimento"]

        # Insert new produtor
        rv = self.client().post('/Produtor/', data=self.produtor)
        self.assertEqual(rv.status_code, 201)

        # Update produtor
        rv = self.client().put('/Produtor/1', data=updated_data)
        self.assertEqual(rv.status_code, 200)

        # Get same produtor and check if the name has changed.
        results = self.client().get('/Produtor/1')
        res_json = json.loads(results.data.decode('utf-8').replace("'", "\""))
        
        self.assertEqual(updated_data["nrDocumento"], res_json["nrDocumento"])
        self.assertEqual(updated_data["nmProdutor"], res_json["nmProdutor"])
        self.assertEqual(updated_data["nrTelefone"], res_json["nrTelefone"])
        self.assertEqual(updated_data["dsEmail"], res_json["dsEmail"])
        self.assertEqual(updated_data["cdEstabelecimento"], res_json["cdEstabelecimento"])


    def test_produtor_deletion(self):
        """Test API can delete an existing produtor. (DELETE request)."""

        # Create a new estabelecimento
        estab = self.client().post('/Estabelecimento/', data=self.estabelecimento)
        estab_json = json.loads(estab.data.decode('utf-8').replace("'", "\""))
        self.assertEqual(estab.status_code, 201)

        # Assign estabelecimento to produtor
        self.produtor["cdEstabelecimento"] = estab_json["idEstabelecimento"]
        
        # Create new produtor
        rv = self.client().post('/Produtor/', data=self.produtor)
        self.assertEqual(rv.status_code, 201)

        # Delete produtor created earlier
        res = self.client().delete('/Produtor/1')
        self.assertEqual(res.status_code, 200)

        # Test to see if it exists, should return a 404
        result = self.client().get('/Produtor/1')
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