import random
import  art
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
while(True):
    user_choice = input("Do you wanna play a game of Blackjack? Type 'y' or 'n': ").lower()
    if user_choice == "y":
        player = []
        computer = []
        print(art.logo)
        player.append(cards[random.randint(0,len(cards)-1)])
        player.append(cards[random.randint(0, len(cards)-1)])
        computer.append(cards[random.randint(0, len(cards)-1)])
        print(f"Your cards: {player}, current score: {sum(player)}")
        print(f"Computer's first card: {computer[0]}")
        if sum(player)==21:
            print(f"Your final hand: {player}, final score: {sum(player)}")
            print(f"Computer's final hand: [{computer[0]}], final score: {computer[0]}")
            print("Win with a Blackjack 😎")
            continue
        while(True):
            user_choice=input("Type 'y' to get another card ,type 'n' to pass: ")
            computer.append(cards[random.randint(0, len(cards) - 1)])
            if user_choice == "y":
                player.append(cards[random.randint(0, len(cards)-1)])
                print(f"Your cards: {player}, current score: {sum(player)}")
                print(f"Computer's first card: {computer[0]}")
                if sum(player) > 21:
                    print(f"Your final hand: {player}, final score: {sum(player)}")
                    print(f"Computer's final hand: [{computer[0]}], final score: {computer[0]}")
                    print("You loose 😭")
                    break
                elif sum(player)==21:
                    print(f"Your final hand: {player}, final score: {sum(player)}")
                    print(f"Computer's final hand: [{computer[0]}], final score: {computer[0]}")
                    print("Win with a Blackjack 😎")
                    break
                else:
                    continue
            else:
                print(f"Your final hand: {player}, final score: {sum(player)}")
                print(f"Computer's final hand: {computer}, final score: {sum(computer)}")
                if sum(player) > sum(computer):
                    print("You win 🏅")
                elif sum(player) == sum(computer):
                    print("Draw 🙂")
                elif sum(computer) >  21:
                    print("You win 🏅")
                else:
                    print("You loose 😭")
                break
    else:
        break





