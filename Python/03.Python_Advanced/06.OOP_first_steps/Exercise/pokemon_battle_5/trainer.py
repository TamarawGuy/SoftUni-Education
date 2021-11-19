class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon):
        if pokemon not in self.pokemon:
            self.pokemon.append(pokemon)
            return f"Caught {pokemon.name} with health {pokemon.health}"

        return "This pokemon is already caught"

    def release_pokemon(self, pokemon_name):
        if pokemon_name in [p.name for p in self.pokemon]:
            pokemon = [p for p in self.pokemon if p.name == pokemon_name][0]
            self.pokemon.remove(pokemon)
            return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        result = f"Pokemon Trainer {self.name}\n"
        result += f"Pokemon count {len(self.pokemon)}\n"
        for pokemon in self.pokemon:
            result += "- " + pokemon.pokemon_details() + "\n"

        return result
