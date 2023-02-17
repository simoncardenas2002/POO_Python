import time
import sys


def factorial(n):
    respuesta=1

    while n>1:
        respuesta *= n
        n -=1

    return respuesta

def factorial_recursive(n):
    if n==1:
        return 1
    
    return n* factorial_recursive(n-1)


if __name__ == '__main__':
    n=1000
    sys.setrecursionlimit(n + 1000)

    comienzo=time.time()
    factorial(n)
    final=time.time()
    print(final -comienzo)

    comienzo=time.time()
    factorial_recursive(n)
    final=time.time()
    print(final -comienzo)
