from unittest import TestCase
from application import get_app


class PokemonTest(TestCase):
    def setUp(self):
        self.application = get_app()        # get application from application.py
        self.client = self.application.test_client()    # create a test client for our application

    def test_get_pokemon(self):
        response = self.client.get("/pokemon/Charmander")
        print(response.json)
        self.assertTrue(200, response.status_code)
        self.assertTrue(response.get_json().get('types')[0] == 'fire')

    def test_get_pokemon_types(self):
        response = self.client.get("/pokemon/Charizard")
        print(response.json)
        self.assertTrue(200, response.status_code)
        self.assertTrue(response.get_json().get('types')[0] == 'fire')
        self.assertTrue(response.get_json().get('types')[1] == 'flying')

    def test_get_pokemon(self):
        response = self.client.get("/pokemon/Starmie")
        print(response.json)
        self.assertTrue(200, response.status_code)
        self.assertTrue(response.get_json().get('types')[0] == 60)
        self.assertTrue(response.get_json().get('stats').get('attack') == 75)
        self.assertTrue(response.get_json().get('stats').get('hp') == 60)
        self.assertTrue(response.get_json().get('stats').get('attack') == 75)
        self.assertTrue(response.get_json().get('stats').get('defense') == 85)
        self.assertTrue(response.get_json().get('stats').get('special_attack') == 100)







