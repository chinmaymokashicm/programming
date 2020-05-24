def factorial(n):
    if(n == 0):
        return(1)
    else:
        return(n * factorial(n - 1))


def factorial_for(n):
    answer = 1
    for i in range(1, n+1):
        answer = answer * i
    return(answer)

# print(factorial(5))

import time

def call(n):
    start = time.time()
    answer = factorial(n)
    end = time.time()
    t_reqd = end - start
    print(f'Factorial of {n} is {answer}. It took {int(t_reqd)} seconds for recursion')

    start = time.time()
    answer = factorial_for(n)
    end = time.time()
    t_reqd = end - start
    print(f'Factorial of {n} is {answer}. It took {int(t_reqd)} seconds for for loop')


call(500)