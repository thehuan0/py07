import random
from ex0.Card import Card
# from ex1.SpellCard import SpellCard
# from ex1.ArtifactCard import ArtifactCard


class Deck:
    def __init__(self):
        self._cards = []

    def add_card(self, card: Card) -> None:
        """Adds any card that inherits from the base Card class."""
        if not isinstance(card, Card):
            raise TypeError("Only Card objects can be added to the deck")
        self._cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        """Removes a card by name and returns success status."""
        for card in self._cards:
            if card.name == card_name:
                self._cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        """Randomizes the order of the deck."""
        random.shuffle(self._cards)

    def draw_card(self) -> Card:
        """Removes and returns the top card of the deck."""
        if not self._cards:
            raise IndexError("Cannot draw from an empty deck")
        return self._cards.pop()

    def get_deck_stats(self) -> dict:
        stats = {
            'total_cards': len(self._cards),
            'creatures': 0,
            'spells': 0,
            'artifacts': 0,
            'avg_cost': 0.0
        }
        if not self._cards:
            return stats

        total_cost = 0
        for card in self._cards:
            total_cost += card.cost
            if card.__class__.__name__ == "CreatureCard":
                stats['creatures'] += 1
            elif card.__class__.__name__ == "SpellCard":
                stats['spells'] += 1
            elif card.__class__.__name__ == "ArtifactCard":
                stats['artifacts'] += 1
        stats['avg_cost'] = total_cost / len(self._cards)
        return stats
