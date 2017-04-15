from numpy import array

def vector(*bits):
    return array([ *bits ])

def char_vector_map(alphabet):
    " return a map of characters to bit vectors "
    span = range(len(alphabet) -1)
    return {alphabet[index]: vector(i == index for i in span)
            for index in span}

def vector_char_map(alphabet):
    " return a map of bit vectors to characters "
    span = range(len(alphabet) -1)
    return {vector(i == index for i in span): alphabet[index]
            for index in span}

class BitTensorTranslator:
    " build a tensor([bit array]) <-> string translator "

    def to_tensor(self, string):
        return [self._char_vector_map[c] for c in string]

    def to_string(self, tensor):
        return ''.join([self._vector_char_map[vector] for vector in tensor])

    def __init__(self, alphabet):
        self._char_vector_map = char_vector_map(alphabet)
        self._vector_char_map = vector_char_map(alphabet)
