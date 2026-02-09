from ex0.Card import Rarity
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


def main():
    print("=== DataDeck Deck Builder ===")
    deck = Deck()

    deck.add_card(CreatureCard("Fire Dragon", 5, Rarity.LEGENDARY, 7, 5))
    deck.add_card(SpellCard("Lightning Bolt", 3, Rarity.COMMON, "damage"))
    deck.add_card(ArtifactCard("Mana Crystal", 2, Rarity.RARE, 2, "+1 mana"))

    print("\nBuilding deck with different card types...")
    print(f"Deck stats: {deck.get_deck_stats()}")

    print("\nDrawing and playing cards:")
    deck.shuffle()

    played_cards = []
    try:
        while True:
            card = deck.draw_card()
            type_label = card.__class__.__name__.replace("Card", "")
            print(f"\nDrew: {card.name} ({type_label})")
            print(f"Play result: {card.play({})}")
            played_cards.append(card)
    except IndexError:
        print("\n--- Testing Rigorous State Management ---")

    for card in played_cards:
        if isinstance(card, SpellCard):
            print(f"Re-casting {card.name}: {card.play({})}")
        elif isinstance(card, ArtifactCard):
            print(f"Activating {card.name} (Use 1): {card.activate_ability()}")
            print(f"Activating {card.name} (Use 2): {card.activate_ability()}")
            print(f"Activating {card.name} "
                  f"(Broken check): {card.activate_ability()}")

    print("\nPolymorphism in action: "
          "Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
