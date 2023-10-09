from functools import reduce

n = int(input())
words = input().split()

def get_numbers_of_vowels_in_word(word):
    return 1 if sum(word.count(vowel) for vowel in 'aeiouy') % 2 else 2

print(reduce(lambda acc, word: acc + get_numbers_of_vowels_in_word(word), words, 0))
