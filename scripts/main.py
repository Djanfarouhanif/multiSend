import random

def draw_card():
    """Tirer une carte aléatoire."""
    return random.choice(['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'])

def calculate_score(cards):
    """Calculer le score des cartes."""
    score = 0
    num_aces = 0
    for card in cards:
        if card.isdigit():
            score += int(card)
        elif card in ['J', 'Q', 'K']:
            score += 10
        elif card == 'A':
            num_aces += 1
            score += 11
    while score > 21 and num_aces:
        score -= 10
        num_aces -= 1
    return score

def play_blackjack():
    """Jouer au blackjack."""
    print("Bienvenue au blackjack !")
    player_cards = [draw_card(), draw_card()]
    dealer_cards = [draw_card(), draw_card()]
    print("Vos cartes:", player_cards)
    print("Carte visible du croupier:", dealer_cards[0])
    
    # Player's turn
    while True:
        player_score = calculate_score(player_cards)
        if player_score == 21:
            print("Blackjack ! Vous gagnez !")
            return
        elif player_score > 21:
            print("Vous avez dépassé 21. Vous avez perdu.")
            return
        else:
            action = input("Voulez-vous prendre une autre carte ? (o/n): ").lower()
            if action == 'o':
                player_cards.append(draw_card())
                print("Vos cartes:", player_cards)
            else:
                break
    
    # Dealer's turn
    print("Croupier's turn")
    print("Les cartes du croupier sont:", dealer_cards)
    while calculate_score(dealer_cards) < 17:
        dealer_cards.append(draw_card())
        print("Les cartes du croupier sont:", dealer_cards)
    
    # Determine the winner
    player_score = calculate_score(player_cards)
    dealer_score = calculate_score(dealer_cards)
    print("Votre score:", player_score)
    print("Score du croupier:", dealer_score)
    if player_score > dealer_score or dealer_score > 21:
        print("Félicitations, vous gagnez !")
    elif player_score < dealer_score:
        print("Désolé, vous perdez.")
    else:
        print("Égalité.")

if __name__ == "__main__":
    play_blackjack()
