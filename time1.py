from random import randint 
from time import sleep

def createDeck():
    a = ['2', '3', '4', '5', '6', '7', '8', '9', '10','J', 'Q', 'K', 'A']
    b = ['s', 'h', 'd', 'c']
    c = []

    for i in a :
        for j in b :
            s = i + j
            c.append(s)
    return c

list_of_card = createDeck()

def shuffle():
    for i in range(len(list_of_card)):    ### check after the right of function 
        a = randint(0, 51)
        if a > i :
            item1 = list_of_card[i]
            item2 = list_of_card[a]
            list_of_card.remove(item1)
            list_of_card.remove(item2)
            list_of_card.insert(i, item2)
            list_of_card.insert(a, item1)
        else :
            a = randint(0, 51)
    print(list_of_card)

print(list_of_card)
sleep(1)
shuffle()


def asd(x):
    return 'Ok' if x > 5 else  'No'


vt = asd(randint(0,10))
print(vt)


def ran():
    n = int(input('Enter amount: '))

    for i in range(1, 2*n + 2):
        if i > n + 1:
            i = -i + 2*n + 2
        lis1 = [j for j in range(i)]
        print(lis1)

ran()


def pas_triangle():
    n = int(input('Enter amount: '))

    for i in range(1, n+1):
        if i == 1 or i == 2:
            lis1 = [j+1 for j in range(i)]
            lis1 = [1 for j in range(i)]
        else:
            lis = [j+1 for j in range(int(i/2)+1)]
            lis2 = [j+1 for j in range(i-2)]
            lis1 = lis + lis2
        print(lis1)

pas_triangle()
        

