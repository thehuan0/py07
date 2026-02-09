from abc import ABC, abstractmethod


class Combatable(ABC):
    @abstractmethod
    def attack(self, target) -> dict:
        """Requirement for any unit capable of melee combat."""
        pass

    @abstractmethod
    def defend(self, incoming_damage: int) -> dict:
        """Requirement for calculating damage mitigation."""
        pass

    @abstractmethod
    def get_combat_stats(self) -> dict:
        """Requirement for exposing unit stats for combat calculation."""
        pass
