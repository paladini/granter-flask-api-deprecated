import unittest
import os
import json
from app import create_app, db


class UnidadeExploracaoTestCase(unittest.TestCase):
    """This class represents the UnidadeExploracao test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.unidadeexp = {
            "nrUnidadeExploracao": 2812,
            "qtCapacidadeAlojamento": 200,
            "csTipoUnidadeExploracao": "UPL",
            "stAtiva": True,
            "csTipoAnimal": "SU",
            "cdEstabelecimento": 1
        }

        # binds the app to the current context
        with self.app.app_context():
            # create all tables
            db.create_all()

    # def test_unidade_exploracao_creation(self):
    #     """Test API can create a UnidadeExploracao (POST request)"""
    #     res = self.client().post('/UnidadeExploracao/', data=self.unidadeexp)
    #     self.assertEqual(res.status_code, 201)
    #     self.assertEqual(2812, str(res.data))

    # def test_api_can_get_all_unidades_exploracao(self):
    #     """Test API can get a UnidadeExploracao (GET request)."""
    #     res = self.client().post('/UnidadeExploracao/', data=self.unidadeexp)
    #     self.assertEqual(res.status_code, 201)
    #     res = self.client().get('/UnidadeExploracao/')
    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(2812, str(res.data))

    def test_api_can_get_unidade_exploracao_by_id(self):
        """Test API can get a single UnidadeExploracao by using it's idUnidadeExploracao."""
        
        # Insert new UnidadeExploracao
        rv = self.client().post('/UnidadeExploracao/', data=self.unidadeexp)
        self.assertEqual(rv.status_code, 201)

        # Get the UnidadeExploracao recently added.
        res_json = json.loads(rv.data.decode('utf-8').replace("'", "\""))
        result = self.client().get('/UnidadeExploracao/{}'.format(res_json['idUnidadeExploracao']))
        res_json = json.loads(result.data.decode('utf-8').replace("'", "\""))

        self.assertEqual(result.status_code, 200)
        self.assertEqual(self.unidadeexp["nrUnidadeExploracao"], res_json["nrUnidadeExploracao"])
        self.assertEqual(self.unidadeexp["qtCapacidadeAlojamento"], res_json["qtCapacidadeAlojamento"])
        self.assertEqual(self.unidadeexp["csTipoUnidadeExploracao"], res_json["csTipoUnidadeExploracao"])
        self.assertEqual(self.unidadeexp["stAtiva"], res_json["stAtiva"])
        self.assertEqual(self.unidadeexp["csTipoAnimal"], res_json["csTipoAnimal"])
        self.assertEqual(self.unidadeexp["cdEstabelecimento"], res_json["cdEstabelecimento"])

        # self.assertEqual(2812, str(result.data))

    # def test_unidade_exploracao_can_be_edited(self):
    #     """Test API can edit an existing UnidadeExploracao. (PUT request)"""
    #     rv = self.client().post(
    #         '/UnidadeExploracao/',
    #         data = {
    #             'nrUnidadeExploracao': 2871
    #         }
    #     )
    #     self.assertEqual(rv.status_code, 201)
    #     rv = self.client().put(
    #         '/UnidadeExploracao/1',
    #         data={
    #             'nrUnidadeExploracao': 2812
    #         })
    #     self.assertEqual(rv.status_code, 200)
    #     results = self.client().get('/UnidadeExploracao/1')
    #     self.assertEqual(2812, str(results.data))

    # def test_unidade_exploracao_deletion(self):
    #     """Test API can delete an existing UnidadeExploracao. (DELETE request)."""
    #     rv = self.client().post(
    #         '/UnidadeExploracao/',
    #         data={'nrUnidadeExploracao': 2812})
    #     self.assertEqual(rv.status_code, 201)
    #     res = self.client().delete('/UnidadeExploracao/1')
    #     self.assertEqual(res.status_code, 200)
    #     # Test to see if it exists, should return a 404
    #     result = self.client().get('/UnidadeExploracao/1')
    #     self.assertEqual(result.status_code, 404)

    def tearDown(self):
        """teardown all initialized variables."""
        with self.app.app_context():
            # drop all tables
            db.session.remove()
            db.drop_all()


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()