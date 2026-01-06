import random
import game_data
import art
# Get the data
def lowerOrHiger():
    print(art.logo)
    data = game_data.data
    n = len(data)-1

    # To get a random integer which will be used as random index to get data from game_data
    # 2 indexes, a and b, both should not be equal
    indexA = random.randint(0,n)

    score = 0
    game_ends = False
    while not game_ends:

        # Both indexes must not be same
        indexB = random.randint(0, n)
        if indexB == indexA:
            while indexB == indexA:
                indexB = random.randint(0, n)

        # players
        playerA = data[indexA]['name']
        playerB = data[indexB]['name']

        # Comparison
        # print(f"Compare A: {playerA}, a {data[indexA]['description']}, from {data[indexA]['country']} Followers: {data[indexA]['follower_count']}.")
        print(f"Compare A: {playerA}, a {data[indexA]['description']}, from {data[indexA]['country']}.")
        print(art.vs)
        # print(f"Against B: {playerB}, a {data[indexB]['description']}, from {data[indexB]['country']} Followers: {data[indexB]['follower_count']}.")
        print(f"Against B: {playerB}, a {data[indexB]['description']}, from {data[indexB]['country']}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        comparison = ''
        if guess == 'b':
            comparison = data[indexB]['follower_count'] > data[indexA]['follower_count']
        elif guess == 'a':
            comparison = data[indexA]['follower_count'] > data[indexB]['follower_count']


        # Check if user is right or wrong

        if comparison:
            # To set the value of B to A
            indexA = indexB
            # To count score and print
            score += 1
            print('\n' * 20)
            print(art.logo)
            print(f"You're right! Current score: {score}.")

        else:
            print('\n' * 20)
            print(art.logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            game_ends = True

lowerOrHiger()