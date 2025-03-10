import itertools
import os
import random

def generate_random_combinations(chars, length, num_combinations, output_file):
    combinations = set()
    while len(combinations) < num_combinations:
        combination = ''.join(random.choice(chars) for _ in range(length))
        combinations.add(combination)
    
    with open(output_file, 'w') as file:
        for combo in combinations:
            file.write(combo + '\n')

if __name__ == "__main__":
    chars = "abcdefghijklmnopqrstuvwxyz1234567890._"
    length = int(input("Enter the number of characters for the words: "))
    num_combinations = int(input("Enter the number of combinations you need: "))
    output_file = f"random_combinations_{length}_chars.txt"
    
    generate_random_combinations(chars, length, num_combinations, output_file)
    
    print(f"{num_combinations} random {length}-character combinations have been written to {output_file}")
