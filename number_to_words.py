import inflect
# inflect.py - Correctly generate plurals, singular nouns, ordinals, indefinite articles; convert numbers to words.
def number_to_words(number):
    p = inflect.engine()
    return p.number_to_words(number)

# Example usage

words = number_to_words(int(input('  enter your number ')))
print(words)