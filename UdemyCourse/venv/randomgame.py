import sys
from random import randint
sys.argv

answer = randint(int(sys.argv[1]), int(sys.argv[2]))


while True:
    try:
        print(answer)
        guess = int(input('Guess a number 1-10'))
        if 0 < guess < 11:
            if guess == answer:
                print('That was the right answer!')
                break
        else:
            print('Between 1 and 10')
    except ValueError:
        print('Enter integer')
        continue



        



