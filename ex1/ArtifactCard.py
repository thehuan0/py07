from ex0.Card import Card, Rarity


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int,
                 rarity: Rarity, durability: int, effect: str):
        super().__init__(name, cost, rarity)
        if not isinstance(durability, int) or durability <= 0:
            raise ValueError("Durability must be a positive integer")
        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': f"Permanent: {self.effect}"
            f"(Durability: {self.durability})"
        }

    def activate_ability(self) -> dict:
        if self.durability <= 0:
            return {"error": "Artifact is destroyed and cannot be activated"}

        self.durability -= 1
        return {
            'artifact': self.name,
            'effect_applied': self.effect,
            'remaining_durability': self.durability,
            'is_destroyed': self.durability == 0
        }
