from dataclasses import dataclass
import random
from datetime import datetime
import subprocess

editor = "vim"
now = datetime.now()
filename = f"/home/phil/tmp/alone_among_the_stars_{now.date()}_{now.time()}.md"


@dataclass
class Card:
    suit: str
    rank: str


class Deck:
    ranks = [str(k) for k in range(2, 11)] + "J Q K A".split()
    suits = "Spades Hearts Diamonds Clubs".split()

    def __init__(self):
        self.cards = [Card(suit, rank) for suit in self.suits for rank in self.ranks]
        self.shuffle()

    def __getitem__(self, i):
        return self.cards[i]

    def shuffle(self):
        random.shuffle(self.cards)

    def __len__(self):
        return len(self.cards)

    def draw(self, n):
        cards = self[:n]
        self.cards = self[n:]
        return cards


def roll():
    return random.randint(1, 6)


prompts_ranks = {
    "A": "In a field taller than you.",
    "2": "Under the light of the moon(s).",
    "3": "By a gentle river.",
    "4": "In a steep canyon.",
    "5": "In a treetop.",
    "6": "On the snowy peak of a mountain.",
    "7": "Near a volcano.",
    "8": "On a glacier.",
    "9": "Deep underground.",
    "10": "On a cliff face.",
    "J": "In the desert.",
    "Q": "In deep water.",
    "K": "Floating in the air.",
}

prompts_suits = {
    "Diamonds": """Diamonds are living beings: People like or unlike you, fish,
dinosaurs, wolves, birds, giant insects, etc.""",
    "Clubs": """Clubs are plants and other immobile forms of life: Towering
trees, carnivorous pitchers, giant ferns, glowing weeds,
floating flowers, oozing mushrooms, etc.""",
    "Hearts": """Hearts are ruins: Mysterious obelisks, vine-covered temples,
abandoned dwellings for people bigger than you, a wrecked
spaceship, etc.""",
    "Spades": """Spades are natural phenomena: Huge crystal formations,
mirages, vividly colored lightning, strange clouds, rocks
eroded in strange shapes, veins of precious metals, etc.""",
}

prompts_circumstances = [
    "It is arduous to get to.",
    "You come upon it suddenly",
    "You spot it as you are resting.",
]


def get_prompt(card):
    print(card)
    discovery_type = prompts_suits.get(card.suit)
    discovery_location = prompts_ranks.get(card.rank)
    discovery_circumstances = prompts_circumstances[roll() % 3]

    output = f"\n\nYou discover something. {discovery_circumstances}\n{discovery_type}\nYou find it {discovery_location.lower()}\n\n"
    with open(filename, "a") as f:
        f.write(output)
    subprocess.run([editor, filename])


def discover_planet(deck):
    discoveries = roll()
    if discoveries > len(deck):
        discoveries = len(deck)
    text = f"\nYou discover a new planet with {discoveries} features.\n"

    with open(filename, "a") as f:
        f.write(text)

    cards = deck.draw(discoveries)

    for card in cards:
        get_prompt(card)


def main():
    play = True
    deck = Deck()
    subprocess.run(["touch", filename])
    while play and len(deck) > 0:
        discover_planet(deck)
        still_play = False
        while still_play not in ("1", "2"):
            prompt = "Do you still want to play?\n1: Yes\n2: No\n"
            still_play = input(prompt)
        play = still_play == "1"


if __name__ == "__main__":
    main()
