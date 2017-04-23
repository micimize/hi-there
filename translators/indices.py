from numpy import float32

def char_index_map(alphabet):
    " returns a map of characters to indices in alphabet list"
    return {alphabet[index]: float32(index) for index in range(len(alphabet))}

class TensorTranslator:
    " build a tensor([bit array]) <-> string translator "

    def to_tensor(self, string):
        " convert a string in the target alphabet to an array of indices "
        return [self._char_index_map[c] for c in string]

    def to_string(self, tensor):
        " convert a bit vector built with this translator back to a string "
        return ''.join([
            self._alphabet[int(index)] for index in tensor])

    def __init__(self, alphabet):
        self._char_index_map = char_index_map(alphabet)
        self._alphabet = alphabet
