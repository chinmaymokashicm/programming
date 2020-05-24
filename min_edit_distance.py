# Finding the minimum number of edits on X to get to Y.
# Inserting a new character or deleting an existing character costs 1 edit.
# Substituting costs 2( or 1) edits.

# def update_memo(a, b, memo):
#     memo.update([(a, b)])
#     return

# import functools as ft

# @ft.lru_cache(maxsize=None)





def call_counter(func):
    def helper(*args, **kwargs):
        helper.calls += 1
        return func(*args, **kwargs)
    helper.calls = 0
    helper.__name__= func.__name__

    return helper

def memoize(func):
    mem = {}
    def memoizer(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in mem:
            mem[key] = func(*args, **kwargs)
        return mem[key]
    return memoizer

@call_counter
@memoize
def d(x, y):
    if(len(x) == 0):
        return(len(y)) 
    elif(len(y) == 0):
        return(len(x))
    else:
        return(min(
            d(x[1:], y) + 1,
            d(x, y[1:]) + 1,
            d(x[1:], y[1:]) + (lambda a, b: 0 if a[0] == b[0] else 10)(x, y)
        ))

import time

def call(a, b):
    start = time.time()
    distance = d(a, b)
    end = time.time()
    t_reqd = end - start
    print(f'Minimum distance between {a} and {b} is {distance}. It took {int(t_reqd)} seconds.')

# print(d("Python", "Peithen"))
# print("The function was called " + str(d.calls) + " times!")

# call('abc', 'c')
# call('intention', 'execution')
# call('sunday', 'saturday')
# call('accomodate', 'accommodate')
# call('pharoah', 'pharaoh')
# call('ATGCGTGGCATGGCA', 'ATCCGCGGAGCTACCT')
call('ATGCGTGGCATGGCAGGCTAAATT', 'ATCCGCCCGTGGTACGGAGCTACCT')
# call("Python", "Peithen")