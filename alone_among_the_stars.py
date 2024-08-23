#!/usr/bin/env python

import subprocess
from settings import filename, editor
from classes import Deck
from functions import discover_planet


def main():
    play = True
    deck = Deck()
    # create the file in the tmp folder
    subprocess.run(["touch", filename])

    # check we still want to play and there are cards in the deck
    while play and len(deck) > 0:
        discover_planet(deck)
        still_play = False
        while still_play not in ("1", "2"):  # keep prompting for "1" or "2"
            prompt = "Do you still want to play?\n1: Yes\n2: No\n"
            still_play = input(prompt)
        play = still_play == "1"
    # Open the file one last time
    subprocess.run([editor, filename])


if __name__ == "__main__":
    main()
