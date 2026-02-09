#!/usr/bin/env python3
from abc import ABC, abstractmethod
from enum import Enum
# from typing import Any


class Rarity(Enum):
    COMMON = "Common"
    UNCOMMON = "Uncommon"
    RARE = "Rare"
    LEGENDARY = "Legendary"


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: Rarity):
        if not name or not isinstance(name, str):
            raise ValueError("Card name must be a non-empty string")
        if not isinstance(cost, int) or cost < 0:
            raise ValueError("Card cost must be a non-negative integer")
        if not isinstance(rarity, Rarity):
            raise ValueError("Rarity must be a member of the Rarity Enum")

        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        """Abstract method to be implemented by concrete card types."""
        pass

    def get_card_info(self) -> dict:
        """Returns the base blueprint of any card."""
        return {
            'name': self.name,
            'cost': self.cost,
            'rarity': self.rarity.value
        }

    def is_playable(self, available_mana: int) -> bool:
        """Checks if mana cost is covered."""
        return self.cost <= available_mana
