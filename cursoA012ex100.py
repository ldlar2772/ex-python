import random
import time
l = []
def sort(n):
    for i in range(5):
        x = random.randint(1,n)
        l.append(x)
    for z in l:
        print(z,end=' ',flush=True)
        time.sleep(0.25)
        
sort(5)
def par():
    s=0
    for z in l:
        if z %2==0:
            s+=z
    print(f'\nos valores são {l} a soma é: {s}')
par()