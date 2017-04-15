import random
from itertools import permutations

def alphabet(phrases):
    return list(set(''.join(phrases)))

def signature(phrase):
    return ''.join(sorted(list(phrase)))

def signatures(phrases):
    return {signature(phrase): phrase
            for phrase in phrases}

def max_phrase_length(phrases):
    return len(max(phrases, key=len))

def shuffle_string(string):
    l = list(string)
    random.shuffle(l)
    return ''.join(l)

class AlphabetScramble:
    """
    Given a set of acceptable phrases and a rejection statement
    Bundles all utilities necessary for generating test data
    """

    def random_letter(self):
        return random.choice(self.alphabet)

    def random_scramble(self):
        return ''.join([
            self.random_letter()
            for i in range(self._max_phrase_length) #random.randint(1, self._max_phrase_length))
        ])

    def solve(self, phrase, reject=False):
        return self._signatures.get(
                signature(phrase),
                reject and self.rejection)

    def invalid_scramble(self):
        phrase = self.random_scramble()
        while self.solve(phrase):
            phrase = self.random_scramble()
        return phrase, len(self.alphabet) #self.rejection

    def valid_scramble(self):
        index = random.randint(0, len(self.phrases) - 1)
        return shuffle_string(self.phrases[index]), index

    def scramble(self):
        return random.choice([
            self.invalid_scramble,
            self.valid_scramble ])()

    def __init__(self, phrases, rejection=''):
        self.phrases = phrases
        self.alphabet = alphabet(phrases)
        self.rejection = rejection
        self._signatures = signatures(phrases)
        self._max_phrase_length = max_phrase_length(phrases)

