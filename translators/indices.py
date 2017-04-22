from numpy import array

def bit_vectorizer(alphabet):
    span = range(len(alphabet))
    def bit_vector(index):
        return array([i == index for i in span])
    return span, bit_vector

def char_vector_map(alphabet):
    " return a map of characters to bit vectors "
    span, vector = bit_vectorizer(alphabet)
    return {alphabet[index]: vector(index) for index in span}

def vector_char_map(alphabet):
    " return a map of bit vectors to characters "
    span, vector = bit_vectorizer(alphabet)
    return {vector(index).data.hex(): alphabet[index] for index in span}

def char_index_map(alphabet):
    " returns a map of characters to indices in alphabet list"
    return {alphabet[index]: index for index in range(len(alphabet))}

class TensorTranslator:
    " build a tensor([bit array]) <-> string translator "

    def to_tensor(self, string):
        " convert a string in the target alphabet to an array of indices "
        return [self._char_index_map[c] for c in string]

    def to_string(self, tensor):
        " convert a bit vector built with this translator back to a string "
        return ''.join([
            self._alphabet[index] for index in tensor])

    def __init__(self, alphabet):
        self._char_index_map = char_index_map(alphabet)
        self._alphabet = alphabet
