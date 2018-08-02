from unittest import TestCase
from application import get_app


class RumorMillTest(TestCase):
    def setUp(self):
        self.application = get_app()
        self.client = self.application.test_client()

    # Test to get pokemon's status by input a name
    def test_get_pokemon(self):
        response = self.client.get("/pokemon/Pikachu")
        # print(response.get_json().get('types'))
        self.assertTrue(200, response.status_code)
        self.assertTrue(response.get_json().get('types') == ['electric'])

    # Test to get pokemon's status by input a type
    def test_get_pokemon_type(self):
        response = self.client.get("/pokemon/types/bug")
        # print(response.get_json().get('Accelgor').get('types'))
        self.assertTrue(200, response.status_code)
        self.assertTrue(response.get_json().get('Accelgor').get('types') == ['bug'])

    # Test to get pokemon's status by input two types
    def test_get_pokemon_two_types(self):
        response = self.client.get("/pokemon/types/grass/ice")
        # print(response.get_json().get('Abomasnow').get('types'))
        self.assertTrue(200, response.status_code)
        self.assertTrue(response.get_json().get('Abomasnow').get('types') == ['grass', 'ice'])

    # Test to get pokemon's status by input a hp level
    def test_get_pokemon_hp(self):
        response = self.client.get("/pokemon/stats/hp/50")
        # print(response.get_json())
        self.assertTrue(200, response.status_code)
        self.assertTrue(response.get_json().get('Aron').get('types') == ['rock', 'steel'])

    # Test to get pokemon's status by input attack value
    def test_get_pokemon_attack(self):
        response = self.client.get("/pokemon/stats/attack/50")
        # print(response.get_json())
        self.assertTrue(200, response.status_code)
        self.assertTrue(response.get_json().get('Aegislash').get('types') == ['steel', 'ghost'])

    # Test to get pokemon's status by input defense value
    def test_get_pokemon_defense(self):
        response = self.client.get("/pokemon/stats/defense/60")
        # print(response.get_json())
        self.assertTrue(200, response.status_code)
        self.assertTrue(response.get_json().get('Absol').get('types') == ['dark'])

    # Test to get pokemon's status by input special_attack value
    def test_get_pokemon_special_attack(self):
        response = self.client.get("/pokemon/stats/special_attack/50")
        # print(response.get_json())
        self.assertTrue(200, response.status_code)
        self.assertTrue(response.get_json().get('Aegislash').get('types') == ['steel', 'ghost'])

    # Test to get pokemon's status by input special_defense value
    def test_get_pokemon_special_defense(self):
        response = self.client.get("/pokemon/stats/special_defense/50")
        # print(response.get_json())
        self.assertTrue(200, response.status_code)
        self.assertTrue(response.get_json().get('Anorith').get('types') == ['bug', 'rock'])

    # Test to get pokemon's status by input a speed
    def test_get_pokemon_speed(self):
        response = self.client.get("/pokemon/stats/speed/50")
        # print(response.get_json())
        self.assertTrue(200, response.status_code)
        self.assertTrue(response.get_json().get('Aggron').get('types') == ['rock', 'steel'])

