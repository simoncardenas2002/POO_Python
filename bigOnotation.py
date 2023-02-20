#recursividad múltiple
#Fibonnacci

import time 

def fibonnaci(n):
    if n == 0 or n==1:
        return 1
    else:
        return fibonnaci(n-1) + fibonnaci(n-2)

#O(n^2)
if __name__ == '__main__':
    comienzo=time.time()
    fibonnaci(10)
    final=time.time()
    print ( final-comienzo)
