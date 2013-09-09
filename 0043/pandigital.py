'''
In mathematics, a pandigital number is an integer that in a
given base has among its significant digits each digit used
in the base at least once. For example, 1223334444555567890
is a pandigital number in base 10.
'''
class PandigitalNumber:

    '''
    the valid characters that can be used in a specific base value
    '''
    VALID_CHARACTERS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    '''
    the maximum possible base value
    '''
    MAX_BASE_VALUE = len(VALID_CHARACTERS)

    '''
    takes a string as a pandigital number in the given
    base (base 10 by default)
    '''
    def __init__(self, number, base=10):
        if base > self.MAX_BASE_VALUE or base <= 1:
            raise ValueError("Not a valid base: " + str(base))
        if self._is_pandigital(number, base):
            self.number = number
            self.base = base
        else:
            raise ValueError("Not a pandigital number: " + number)

    '''
    Checks if the integer in the given base is a valid
    pandigital number
    '''
    def _is_pandigital(self, number, base):
        number_map = {}
        
        for char in self.VALID_CHARACTERS[:base]:
            number_map[char] = 0

        for n in number:
            number_map[n] += 1

        # all valid characters in this base must exist
        for n in self.VALID_CHARACTERS[:base]:
            if number_map[n] == 0:
                return False
        return True
