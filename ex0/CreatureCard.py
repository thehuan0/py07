from ex0.Card import Card, Rarity


class CreatureCard(Card):
    def __init__(
            self,
            name: str,
            cost: int,
            rarity: Rarity,
            attack: int,
            health: int
            ):
        super().__init__(name, cost, rarity)

        if not isinstance(attack, int) or attack <= 0:
            raise ValueError("Attack must be a positive integer")
        if not isinstance(health, int) or health <= 0:
            raise ValueError("Health must be a positive integer")

        self.attack = attack
        self.health = health

    def get_card_info(self) -> dict:
        """Overrides base method to include creature-specific stats."""
        info = super().get_card_info()
        info.update({
            'type': 'Creature',
            'attack': self.attack,
            'health': self.health
        })
        return info

    def play(self, game_state: dict) -> dict:
        """Implements the mandatory play interface."""
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': 'Creature summoned to battlefield'
        }

    def attack_target(self, target: str) -> dict:
        """Simulates creature-to-target combat."""
        return {
            'attacker': self.name,
            'target': target,
            'damage_dealt': self.attack,
            'combat_resolved': True
        }
