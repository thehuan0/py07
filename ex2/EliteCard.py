from ex0.Card import Card, Rarity
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(
            self, name: str, cost: int,
            rarity: Rarity, attack: int,
            health: int, mana: int
            ):
        super().__init__(name, cost, rarity)
        self.attack_val = attack
        self.current_health = health
        self.mana_power = mana
        self._is_alive = True

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        mana_cost = 4
        if self.mana_power < mana_cost:
            return {"error": f"Insufficient mana to cast {spell_name}"}

        self.mana_power -= mana_cost
        return {
            'caster': self.name,
            'spell': spell_name,
            'targets': targets,
            'mana_used': mana_cost,
            'remaining_mana': self.mana_power
        }

    def channel_mana(self, amount: int) -> dict:
        self.mana_power += amount
        return {'channeled': amount, 'total_mana': self.mana_power}

    def defend(self, incoming_damage: int) -> dict:
        if not self._is_alive:
            return {"error": f"{self.name} is already defeated"}
        blocked = 2
        damage_taken = max(0, incoming_damage - blocked)
        self.current_health -= damage_taken

        if self.current_health <= 0:
            self.current_health = 0
            self._is_alive = False
        return {
            'defender': self.name,
            'damage_taken': damage_taken,
            'damage_blocked': blocked,
            'remaining_health': self.current_health,
            'still_alive': self._is_alive
        }

    def get_combat_stats(self) -> dict:
        return {'attack': self.attack_val, 'health': self.current_health}

    def get_magic_stats(self) -> dict:
        return {'mana_power': self.mana_power}

    def play(self, game_state: dict) -> dict:
        return {'card_played': self.name,
                'effect': 'Elite deployment successful'}

    def attack(self, target) -> dict:
        return {'attacker': self.name,
                'target': target, 'damage': self.attack_val}
