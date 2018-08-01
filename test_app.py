from application import Pokemon, Pokemon2Types


assert Pokemon().get(pokemon="Pikachu") == {'types': ['electric'], 'stats': {'hp': 35, 'attack': 55, 'defense': 30, 'special_attack': 50, 'special_defense': 40, 'speed': 90}}
# assert Pokemon2Types().get(types="grass", types2="ice") == '<Response 106107 bytes [200 OK]>'
