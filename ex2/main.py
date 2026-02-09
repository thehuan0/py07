from ex0.Card import Rarity
from ex2.EliteCard import EliteCard


def main():
    print("\n=== DataDeck Ability System ===")

    warrior = EliteCard("Arcane Warrior", 6, Rarity.LEGENDARY, 5, 10, 5)

    print("\nEliteCard capabilities (Interface Check):")
    print(f"Card: "
          f"{[m for m in ['play', 'get_card_info', 'is_playable']
              if hasattr(warrior, m)]}")
    print(f"Combatable: "
          f"{[m for m in ['attack', 'defend', 'get_combat_stats']
              if hasattr(warrior, m)]}")
    print(f"Magical: "
          f"{[m for m in ['cast_spell', 'channel_mana', 'get_magic_stats']
              if hasattr(warrior, m)]}")

    print(f"\nPlaying {warrior.name} (Elite Card):")
    print(warrior.play({}))

    print("\n--- Combat Phase ---")
    print(f"Initial Combat Stats: {warrior.get_combat_stats()}")
    print(f"Attack result: {warrior.attack('Enemy Grunt')}")
    print(f"Defense result (Taking 5 damage): {warrior.defend(5)}")
    print(f"Post-Combat Stats: {warrior.get_combat_stats()}")

    print("\n--- Magic Phase ---")
    print(f"Initial Magic Stats: {warrior.get_magic_stats()}")

    print(f"Spell cast: "
          f"{warrior.cast_spell('Fireball', ['Target A', 'Target B'])}")
    print(f"Mana channel (+3): {warrior.channel_mana(3)}")
    print(f"Final Magic Stats: {warrior.get_magic_stats()}")

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
