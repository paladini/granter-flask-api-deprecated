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
            'nmEstabelecimento': "Um nome qualquer"
        }

        # binds the app to the current context
        with self.app.app_context():
            # create all tables
            db.create_all()

    def test_estabelecimento_creation(self):
        """Test API can create a estabelecimento (POST request)"""
        res = self.client().post('/estabelecimento/', data=self.estabelecimento)
        self.assertEqual(res.status_code, 201)
        self.assertIn('Um nome qualquer', str(res.data))

    def test_api_can_get_all_estabelecimentos(self):
        """Test API can get a estabelecimento (GET request)."""
        res = self.client().post('/estabelecimento/', data=self.estabelecimento)
        self.assertEqual(res.status_code, 201)
        res = self.client().get('/estabelecimento/')
        self.assertEqual(res.status_code, 200)
        self.assertIn('Um nome qualquer', str(res.data))

    def test_api_can_get_estabelecimento_by_id(self):
        """Test API can get a single estabelecimento by using it's id."""
        rv = self.client().post('/estabelecimento/', data=self.estabelecimento)
        self.assertEqual(rv.status_code, 201)
        result_in_json = json.loads(rv.data.decode('utf-8').replace("'", "\""))
        result = self.client().get(
            '/estabelecimento/{}'.format(result_in_json['id']))
        self.assertEqual(result.status_code, 200)
        self.assertIn('Um nome qualquer', str(result.data))

    def test_estabelecimento_can_be_edited(self):
        """Test API can edit an existing estabelecimento. (PUT request)"""
        rv = self.client().post(
            '/estabelecimento/',
            data={'name': 'Um nome inicial'})
        self.assertEqual(rv.status_code, 201)
        rv = self.client().put(
            '/estabelecimento/1',
            data={
                "name": "Um outro nome qualquer"
            })
        self.assertEqual(rv.status_code, 200)
        results = self.client().get('/estabelecimento/1')
        self.assertIn('Um outro nome qualquer', str(results.data))

    def test_estabelecimento_deletion(self):
        """Test API can delete an existing estabelecimento. (DELETE request)."""
        rv = self.client().post(
            '/estabelecimento/',
            data={'name': 'Um outro nome qualquer'})
        self.assertEqual(rv.status_code, 201)
        res = self.client().delete('/estabelecimento/1')
        self.assertEqual(res.status_code, 200)
        # Test to see if it exists, should return a 404
        result = self.client().get('/estabelecimento/1')
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