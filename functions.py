import random
from prompts import *
import subprocess
from settings import filename, editor


def roll():
    return random.randint(1, 6)


def get_prompt(i, card):
    discovery_type = prompts_suits.get(card.suit)
    discovery_location = prompts_ranks.get(card.rank)
    discovery_circumstances = prompts_circumstances[roll() % 3]

    output = f"\n### Feature {i}\n\n>{card}\n>\n>{discovery_type}\n>\n>You find it {discovery_location.lower()}\n>\n>{discovery_circumstances}\n\n"
    with open(filename, "a") as f:
        f.write(output)
    subprocess.run([editor, filename])


def discover_planet(deck):
    discoveries = roll()
    if discoveries > len(deck):
        discoveries = len(deck)
    text = f"\n## You discover a new planet with {discoveries} features.\n"

    with open(filename, "a") as f:
        f.write(text)

    cards = deck.draw(discoveries)

    for i, card in enumerate(cards, start=1):
        get_prompt(i, card)
