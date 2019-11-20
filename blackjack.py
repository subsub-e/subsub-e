import random
def fresh_deck():
    suits = {"Spade", "Heart", "Diamond", "Club"}
    ranks = {"A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"}
    deck = []
    for key in suits:
        for keys in ranks:
            card = {"suit": key, "rank": keys}
            deck = deck + [card]
    random.shuffle(deck)
    return deck

def hit(deck):
    if deck == []:
        return fresh_deck()
    return deck[0], deck[1:]

def count_score(cards):
    score = 0
    number_of_ace = 0
    for card in cards:
        if card['rank'] == 'A':
            score += 11
            number_of_ace += 1
        elif card['rank'] in {'K', 'Q', 'J'}:
            score += 10
        else:
            score += card['rank']
    while score > 21:
        if number_of_ace > 0:
            score -= 10
            number_of_ace -= 1
        if number_of_ace == 0:
            break
    return score

def show_cards(cards, message):
    print(message)
    for card in cards:
        print(card["suit"], card["rank"])

def more(message):
    answer = input(message)
    while not ('y' or 'n'):
        answer = input(message)
    if answer == 'y':
        return True
    else:
        return False

def blackjack():
    print("Welcome to SMaSH Casino!")
    chips = 0
    chips = play_game(chips)
    while more("Play more? (y/n)"):
        chips = play_game(chips)
    print("Bye!")

def play_game(chips):
    print("——---")
    deck = fresh_deck()
    dealer = []
    player = []
    (card, deck) = hit(deck)
    player.append(card)
    (card, deck) = hit(deck)
    dealer.append(card)
    (card, deck) = hit(deck)
    player.append(card)
    (card, deck) = hit(deck)
    dealer.append(card)
    print("My cards are:")
    print(" ", "****", "**")
    print(" ", dealer[1]["suit"], dealer[1]["rank"])
    show_cards(player, "Your cards are:")
    score_player = count_score(player)
    score_dealer = count_score(player)
    if score_player == 21:
        chips +=  2
        print("Blackjack! You won.")
        print("Chips = ",chips)
        return chips
    while score_player < 21 and more("Hit? (y/n)"):
        (card, deck) = hit(deck)
        player.append(card)
        print(" ", player[-1]["suit"], player[-1]["rank"])
        score_player = count_score(player)
    if score_player > 21:
        print("You bust! I won.")
        chips -= 1
        print("Chips = ",chips)
        return chips
    while score_dealer <= 16:
        (card, deck) = hit(deck)
        dealer.append(card)
        score_dealer = count_score(dealer)
    show_cards(dealer, "My cards are:")
    if score_dealer > 21:
        print("I bust! You won.")
        chips += 1
        print("Chips =", chips)
        return chips
    elif score_dealer > score_player:
        print("I won.")
        chips -= 1
        print("Chips =", chips)
        return chips
    elif score_dealer < score_player:
        print("You won.")
        chips += 1
        print("Chips =", chips)
        return chips
    else:
        print("We draw.")
        print("Chips =", chips)
        return chips
