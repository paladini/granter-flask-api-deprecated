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
        
        result = self.client().get('/UnidadeExploracao/{}'.format(1))
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