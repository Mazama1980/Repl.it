"""
2022-01-24 -- Fundamentals

Agenda
------

* Expression exercise
* Problem solving exercise
    - generate a deck of cards
* Review datetimes
    - today's date
    - 
* datetimes
    - 


"""

# Genrate a list of strings representing a deck of 52 playing cards
#    where the first character represents the face and the second represents the suit
#    For example: "3S" is the 3 of spades
#    Suits: D, H, C, and S
#    Faces: 2-9, T, J, Q, K and A

def deck():
    deck_number = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    deck_suit = ["D", "H", "C", "S"]

    cards = []
    for card in deck_number:
        card = cards.append


deck()

Suits = ["D", "H", "S", "C"]
Faces = ["2","3","4","5","6","7","8","9", "T", "J", "Q", "K", "A"]
Whole_Deck = []


def card_deck():
    for face in Faces:
        for suit in Suits:
            card = face + suit
            Whole_Deck.append(f"{card}")
    print(Whole_Deck)


card_deck()
