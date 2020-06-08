import sys
from functools import wraps


""" 
All NLP algorithms I practise should be found here.
"""

class Decorators:
    # Memoization decorator function
    def memoize(f):
        memo = {}
        @wraps(f)
        def memoizer(*args, **kwargs):
            key = str(args) + str(kwargs)
            if(key not in memo):
                memo[key] = f(*args, **kwargs)
            return(memo[key])
        return(memoizer)

    # Wrapper on abbreviation function
    def yes_or_no(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            answer = f(*args, **kwargs)
            if(answer):
                return('YES')
            else:
                return('NO')
        return(wrapper)


class NLP:
    """ 
    Only operations allowed: 
    1. Deletion of any lowercase alphabet of a
    2. Capitalize any lowercase alphabet of a 

    If first alphabet of a is capitalized, compare with first aplhabet of b. If equal, compare second alphabet onwards
    If not, return False 
    """

    # @Decorators.yes_or_no
    # @Decorators.memoize
    def abbreviation(self, a, b):
        sys.setrecursionlimit(50000)
        @Decorators.memoize
        def internal_abbr(a, b):
            if(len(a) < len(b)):
                return(False)
            elif(len(b) == 0):
                if(any(char.isupper() for char in a)):
                    return(False)
                else:
                    return(True)
            elif(a[0].isupper()):
                if(a[0] == b[0]):
                    return(internal_abbr(a[1:], b[1:]))
                else:
                    return(False)
            else:
                return(internal_abbr(a[1:], b) or internal_abbr(a[0].capitalize() + a[1:], b))

        return(internal_abbr(a, b))
    
    @Decorators.memoize
    def min_edit_distance(self, x, y, substitution_weight = 1):
        if(len(x) == 0):
            return(len(y)) 
        elif(len(y) == 0):
            return(len(x))
        else:
            return(min(
                self.min_edit_distance(x[1:], y) + 1,
                self.min_edit_distance(x, y[1:]) + 1,
                self.min_edit_distance(x[1:], y[1:]) + (lambda a, b: 0 if a[0] == b[0] else substitution_weight)(x, y)
            ))

