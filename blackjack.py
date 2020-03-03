
import random
# dealer cards

dealer_cards = []

# player cards

player_cards = []

# Deal the cards

#Dealer Cards

while len(dealer_cards) != 2:
    dealer_cards.append(random.randint(1, 11))
    if len(dealer_cards) == 2:
        print("Dealer has X & ", dealer_cards[1])

#Player Cards

while len(player_cards) != 2:
    player_cards.append(random.randint(1,11))
    if len(player_cards) == 2:
        print("Player has:", player_cards)

# Sum of the dealer cards
if sum(dealer_cards ) == 21:
    print("Dealer has 21 & Wins")
elif sum(dealer_cards) > 21:
    print("Dealer has busted")

#Sum of player cards
while sum(player_cards) < 21:
    action_taken = str(input("Do you want to stay or hit?"))
    if action_taken == "hit":
        player_cards.append(random.randint(1,11))
        print("You now have a total of " + str(sum(player_cards))+ " from these cards",player_cards)
    else:
        print("The dealer has a total of " + str(sum(dealer_cards))+" with these cards", dealer_cards)
        print("You have a total of "+str(sum(player_cards))+ " from these cards", player_cards)
        if sum(dealer_cards) > sum(player_cards):
         print("Dealer wins!")
        else:
            print("You win!")
        break


if sum(player_cards) == 21:
    print("You got BlackJack!")
elif sum(player_cards) > 21:
    print("you busted")