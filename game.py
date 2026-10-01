import random

SUITS = ["♠", "♥", "♦", "♣"]
RANKS = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"
]

def create_card(suit, rank):
    """Create a simple card dictionary."""
    return {
        "rank": rank,
        "suit": suit
    }

def card_value(card):
    """Return the value of one card."""
    if card["rank"] == "A":
        return 11
    if card["rank"] in ["J", "Q", "K"]:
        return 10
    return int(card["rank"])

def create_deck():
    """Create 52 cards and shuffle the deck."""
    deck = []
    for suit in SUITS:
        for rank in RANKS:
            deck.append(create_card(suit, rank))
    random.shuffle(deck)
    return deck

def draw_card(game):
    """Remove and return one card from the deck."""
    return game["deck"].pop()

def score(hand):
    """Calculate the value of a hand, handling Aces."""
    total = sum(card_value(card) for card in hand)

    aces = sum(
        1 for card in hand
        if card["rank"] == "A"
    )

    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total

def player_score(game):
    """Return the player's current score."""
    return score(game["player"]) #this gets the player cards and calculate their value

def dealer_score(game):
    """Return the dealer's current score."""
    return score(game["dealer"]) 

def new_game():
    """Create and return a new game."""
    game = {
        "deck": create_deck(), #create hte deck with 52 shuffled cards
        "player": [], #players empty hand
        "dealer": [], #dealers empty hand
        "finished": False,
        "message": "" #no results
    }
    #give the player 2 cards
    #get one card from the deck and put to the player hand
    game["player"].append(draw_card(game))
    game["player"].append(draw_card(game))
    #give the dealer 2 cards
    game["dealer"].append(draw_card(game))
    game["dealer"].append(draw_card(game))

    return game

def hit(game):
    """Give the player one card and check for a bust."""
    if game["finished"]:
        return
    #give player another card
    game["player"].append(draw_card(game))

    if player_score(game) > 21:
        game["finished"] = True
        game["message"] = "Bust! You Lose."

def stand(game):
    """Let the dealer play, then decide the winner."""
    if game["finished"]:
        return
    while dealer_score(game) < 17:
        game["dealer"].append(draw_card(game))
    player = player_score(game)
    dealer = dealer_score(game)

    game["finished"] = True

    if dealer > 21:
        game["message"] = "Dealer Busts! You Win!"
    elif player > dealer:
        game["message"] = "You Win!"
    elif dealer > player:
        game["message"] = "Dealer Wins."
    else:
        game["message"] = "Draw."

def card_to_dict(card):
    """Convert a card into the format expected by the frontend."""
    return {
        "rank": card["rank"],
        "suit": card["suit"],
        "value": card_value(card)
    }

def state(game):
    """Return the public game state for the frontend."""
    if game["finished"]:
        #show all dealer cards
        dealer_cards = [
            card_to_dict(card)
            for card in game["dealer"]
        ]
    else:
        dealer_cards = [
            #the first dealer card is visible
            card_to_dict(game["dealer"][0]),
            {"hidden": True}
        ]

    return {
        #we create dict that will become json
        "player_cards": [
            card_to_dict(card)
            for card in game["player"]
        ],
        "dealer_cards": dealer_cards,
        "player_score": player_score(game),
        "dealer_score":
            dealer_score(game)
            if game["finished"]
            else None,
        "finished": game["finished"],
        "message": game["message"]
    }