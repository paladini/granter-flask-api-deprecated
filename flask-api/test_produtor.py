import unittest
import os
import json
from app import create_app, db


class ProdutorTestCase(unittest.TestCase):
    """This class represents the Produtor test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.produtor = {
            'nmProdutor': "Sebastião Salgado"
        }

        # binds the app to the current context
        with self.app.app_context():
            # create all tables
            db.create_all()

    def test_produtor_creation(self):
        """Test API can create a produtor (POST request)"""
        res = self.client().post('/produtor/', data=self.produtor)
        self.assertEqual(res.status_code, 201)
        self.assertIn('Sebastião Salgado', str(res.data))

    def test_api_can_get_all_produtores(self):
        """Test API can get a produtor (GET request)."""
        res = self.client().post('/produtor/', data=self.produtor)
        self.assertEqual(res.status_code, 201)
        res = self.client().get('/produtor/')
        self.assertEqual(res.status_code, 200)
        self.assertIn('Sebastião Salgado', str(res.data))

    def test_api_can_get_produtor_by_id(self):
        """Test API can get a single produtor by using it's id."""
        rv = self.client().post('/produtor/', data=self.produtor)
        self.assertEqual(rv.status_code, 201)
        result_in_json = json.loads(rv.data.decode('utf-8').replace("'", "\""))
        result = self.client().get(
            '/produtor/{}'.format(result_in_json['id']))
        self.assertEqual(result.status_code, 200)
        self.assertIn('Sebastião Salgado', str(result.data))

    def test_produtor_can_be_edited(self):
        """Test API can edit an existing produtor. (PUT request)"""
        rv = self.client().post(
            '/produtor/',
            data={'name': 'Vincent Van Gogh'})
        self.assertEqual(rv.status_code, 201)
        rv = self.client().put(
            '/produtor/1',
            data={
                "name": "Sebastião Salgado"
            })
        self.assertEqual(rv.status_code, 200)
        results = self.client().get('/produtor/1')
        self.assertIn('Sebastião Salgado', str(results.data))

    def test_produtor_deletion(self):
        """Test API can delete an existing produtor. (DELETE request)."""
        rv = self.client().post(
            '/produtor/',
            data={'name': 'Sebastião Salgado'})
        self.assertEqual(rv.status_code, 201)
        res = self.client().delete('/produtor/1')
        self.assertEqual(res.status_code, 200)
        # Test to see if it exists, should return a 404
        result = self.client().get('/produtor/1')
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