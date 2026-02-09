from abc import ABC, abstractmethod


class Magical(ABC):
    @abstractmethod
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        """Requirement for units with spellcasting capabilities."""
        pass

    @abstractmethod
    def channel_mana(self, amount: int) -> dict:
        """Requirement for units that interact with mana pools."""
        pass

    @abstractmethod
    def get_magic_stats(self) -> dict:
        """Requirement for exposing arcane metrics."""
        pass
