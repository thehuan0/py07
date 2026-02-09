from ex0.Card import Card, Rarity


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: Rarity, effect_type: str):
        super().__init__(name, cost, rarity)
        valid_effects = ["damage", "heal", "buff", "debuff"]
        if effect_type not in valid_effects:
            raise ValueError(f"Effect type must be one of {valid_effects}")
        self.effect_type = effect_type
        self._is_consumed = False

    def play(self, game_state: dict) -> dict:
        if self._is_consumed:
            return {"error": "Spell has already been cast and consumed"}

        self._is_consumed = True
        resolution = self.resolve_effect([])
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': resolution['description']
        }

    def resolve_effect(self, targets: list) -> dict:
        """Generates dynamic descriptions based on the effect_type."""
        descriptions = {
            "damage": f"Deal 3 damage to {len(targets) or 'target'}",
            "heal": f"Restore 5 health to {len(targets) or 'target'}",
            "buff": f"Increase stats of {len(targets) or 'target'} by +2/+2",
            "debuff": f"Reduce stats of {len(targets) or 'target'} by -1/-1"
        }

        return {
            'type': self.effect_type,
            'descrition': descriptions.get(self.effect_type, "Unknown effect"),
            'resolved': True
        }
