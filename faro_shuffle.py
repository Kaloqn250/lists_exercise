deck_of_cards = input().split()
shuffle_count = int(input())

for shuffle in range(shuffle_count):

    middle_of_the_deck = len(deck_of_cards) // 2
    left_pack = deck_of_cards[0:middle_of_the_deck]
    right_pack = deck_of_cards[middle_of_the_deck:]

    after_shuffle_deck = []

    for index in range(len(left_pack)):
        after_shuffle_deck.append(left_pack[index])
        after_shuffle_deck.append(right_pack[index])

    deck_of_cards = after_shuffle_deck

print(deck_of_cards)
