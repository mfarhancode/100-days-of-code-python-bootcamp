import random
import art
def blackjack():

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    uc = [] # User's cards
    cc = [] # Computer's cards
    for i in range(2):
        uc.append(random.choice(cards))
        cc.append(random.choice(cards))
    condition = True
    while condition:
        score_uc = sum(uc)
        score_cc = sum(cc)
        if sum(uc) > 21:
            if 11 in cards:
                cards.remove(11)
                cards.append(1)
        if sum(cc) == 21 and len(cc) == 2:
            print(f"    Your final hand: {uc}, final score: {score_uc}")
            print(f"    Computer's final hand: {cc}, final score: 0")
            print("Lose, opponent has Blackjack 😱")
            condition = False
        elif score_uc == 21 and len(uc) == 2:
            print(f"    Your final hand: {uc}, final score: {0}")
            print(f"    Computer's final hand: [{cc[0]}], final score: {cc[0]}")
            print("Win with a Blackjack 😎")
            condition = False
            return
        if sum(uc) > 21 and 11 in cc:
            temp = cc
            for i in range(len(cc)):
                if cc[i] == 11:
                    cc[i] = 1
            if sum(temp) > 21:
                print('Lose')
                condition = False

        print(f"    Your cards: {uc}, current score: {score_uc}")
        print(f"    Computer's first card: {cc[0]}")

        ask = input("Type 'y' to get another card, type 'n' to pass:").lower()
        if ask == 'n':

            # print(score_uc, score_cc)
            if score_cc < 16:
                while score_cc < 16:
                    cc.append(random.choice(cards))
                    score_cc = sum(cc)
                if score_cc > 21:
                    # print('--')
                    print(f"    Your final hand: {uc}, final score: {score_uc}")
                    print(f"    Computer's final hand: {cc}, final score: {score_cc}")
                    print(f"Opponent went over. You win 😁")
                    condition = False
                else:
                    # print('----')
                    print(f"    Your final hand: {uc}, final score: {score_uc}")
                    print(f"    Computer's final hand: {cc}, final score: {score_cc}")
                    if score_cc > score_uc:
                        print("You lose 😤")
                    elif score_cc < score_uc:
                        print("You win 😤")
                    else:
                        print("Draw 🙃")
                    condition = False
            else:
                # print('------')
                print(f"    Your final hand: {uc}, final score: {score_uc}")
                print(f"    Computer's final hand: {cc}, final score: {score_cc}")
                if score_cc > score_uc:
                    print("You lose 😤")
                elif score_cc < score_uc:
                    print("You win 😤")
                elif score_cc == score_uc:
                    print("Draw 🙃")
                condition = False
        elif ask == 'y':
            uc.append(random.choice(cards))
            score_uc = sum(uc)
            score_cc = sum(cc)
            if score_uc > 21:
                print(f"    Your final hand: {uc}, final score: {score_uc}")
                print(f"    Computer's final hand: [{cc[0]}], final score: {cc[0]}")
                print(f"You went over. You lose 😭")
                condition = False

while input("Do you want to play a game of Blackjack? Type 'y' or 'n':").lower() == "y":
    print(art.logo)
    blackjack()