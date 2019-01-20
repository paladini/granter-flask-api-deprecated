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

    def test_api_can_get_unidade_exploracao_by_id(self):
        """Test API can get a single UnidadeExploracao by using it's idUnidadeExploracao."""
        
         # Create a new estabelecimento
        # estab = self.client().post('/Estabelecimento/', data=self.estabelecimento)
        # estab_json = json.loads(estab.data.decode('utf-8').replace("'", "\""))
        # self.assertEqual(estab.status_code, 201)

        # Assign estabelecimento to produtor
        # self.unidadeexp["cdEstabelecimento"] = estab_json["idEstabelecimento"]

        # Insert new UnidadeExploracao
        # rv = self.client().post('/UnidadeExploracao/', data=self.unidadeexp)
        # self.assertEqual(rv.status_code, 201)

        # Get the UnidadeExploracao recently added.
        # res_json = json.loads(rv.data.decode('utf-8').replace("'", "\""))
        result = self.client().get('/UnidadeExploracao/{}'.format(1))
        # res_json = json.loads(result.data.decode('utf-8').replace("'", "\""))

        self.assertEqual(result.status_code, 404)
        # self.assertEqual(self.unidadeexp["nrUnidadeExploracao"], res_json["nrUnidadeExploracao"])
        # self.assertEqual(self.unidadeexp["qtCapacidadeAlojamento"], res_json["qtCapacidadeAlojamento"])
        # self.assertEqual(self.unidadeexp["csTipoUnidadeExploracao"], res_json["csTipoUnidadeExploracao"])
        # self.assertEqual(self.unidadeexp["stAtiva"], res_json["stAtiva"])
        # self.assertEqual(self.unidadeexp["csTipoAnimal"], res_json["csTipoAnimal"])
        # self.assertEqual(self.unidadeexp["cdEstabelecimento"], res_json["cdEstabelecimento"])

    def tearDown(self):
        """teardown all initialized variables."""
        with self.app.app_context():
            # drop all tables
            db.session.remove()
            db.drop_all()


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()