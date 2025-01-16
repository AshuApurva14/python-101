# Date: 15th January 2025

# This is a simple program that generates a random phrase using three lists of words

# I will use this random phrase in the guessing game program

# The random module provides a random number generator.
# import the random module
import random

# Create three lists , one for verbs, one for nouns, and one for adject
# List of Verbs
verbs = ["go", "eat", "sleep", "jump","run", "walk", "play", "sing", "dance","read"]
# List of adjectives
adjectives = ["big", "small", "tall", "short", "fat", "skinny", "funny", "serious", "happy", "sad"]
# List of nouns
nouns = ["dog", "cat", "ball", "book", "pen", "car", "tree", "house", "apple", "banana"]

verb = random.choice(verbs)
noun = random.choice(nouns)
adjective = random.choice(adjectives)

phrase = verb + " " + adjective + " " + noun

print("Random Phrase:", phrase)
# The choice() method returns a randomly selected element from the specified sequence.
# The join() method takes all items in an iterable and joins them into one string.
