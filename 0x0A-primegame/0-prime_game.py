#!/usr/bin/python3


def isWinner(x, nums):
    # Function to check if a number is prime
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    # Recursive function to simulate the game
    def play_game(player, numbers):
        # Base case: no prime numbers left, current player loses
        if all(not is_prime(num) for num in numbers):
            return "Ben" if player == "Maria" else "Maria"

        # Iterate through the numbers and choose a prime
        for num in numbers:
            if is_prime(num):
                # Remove the chosen prime and its multiples
                new_numbers = [n for n in numbers if n % num != 0]
                # Recursively call the function with the other player
                winner = play_game("Ben" if player == "Maria" else "Maria", new_numbers)
                # If the other player loses, the current player wins
                if winner == player:
                    return player

        # If no winning move is found, the current player loses
        return "Ben" if player == "Maria" else "Maria"

    # Initialize counters for Maria and Ben's wins
    maria_wins = 0
    ben_wins = 0

    # Iterate through each round
    for i in range(x):
        # Get the current round's parameters
        n = nums[i]
        numbers = list(range(1, n + 1))
        # Simulate the game for the current round
        winner = play_game("Maria", numbers)
        # Increment the corresponding player's wins
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1

    # Determine the winner of the most rounds
    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None
