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
            "stAtivo": 1,
            "idCliente": 10
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
        # print(res.data)
        self.assertEqual(self.estabelecimento["nmEstabelecimento"], res_json["nmEstabelecimento"])
        # self.assertEqual(self.estabelecimento, str(res.data))

    def test_api_can_get_all_estabelecimentos(self):
        """Test API can get a estabelecimento (GET request)."""

        # Insert new estabelecimento
        res = self.client().post('/Estabelecimento/', data=self.estabelecimento)
        self.assertEqual(res.status_code, 201)
        
        # Get inserted estabelecimentos
        res = self.client().get('/Estabelecimento/')
        res_json = json.loads(res.data.decode('utf-8').replace("'", "\""))
        
        # self.assertEqual('Granja Santa Clara', str(res.data))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(self.estabelecimento["nmEstabelecimento"], res_json[0]["nmEstabelecimento"])


    def test_api_can_get_estabelecimento_by_id(self):
        """Test API can get a single estabelecimento by using it's id."""
        rv = self.client().post('/Estabelecimento/', data=self.estabelecimento)
        self.assertEqual(rv.status_code, 201)

        res_json = json.loads(rv.data.decode('utf-8').replace("'", "\""))
        result = self.client().get('/Estabelecimento/{}'.format(res_json['idEstabelecimento']))
        self.assertEqual(result.status_code, 200)
        # self.assertIn('Granja Santa Clara', str(result.data))
        self.assertEqual(self.estabelecimento["nmEstabelecimento"], res_json["nmEstabelecimento"])


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
            "stAtivo": 1,
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


    def test_estabelecimento_deletion(self):
        """Test API can delete an existing estabelecimento. (DELETE request)."""
        rv = self.client().post(
            '/Estabelecimento/',
            data={'name': 'Um outro nome qualquer'})
        self.assertEqual(rv.status_code, 201)
        res = self.client().delete('/Estabelecimento/1')
        self.assertEqual(res.status_code, 200)
        # Test to see if it exists, should return a 404
        result = self.client().get('/Estabelecimento/1')
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