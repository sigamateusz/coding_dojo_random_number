import os
import random
os.system('clear') # clear screen

def wrong_choice():
    global my_number
    try:
        my_number = int(input('What is your guess? '))
    except ValueError:
        print('Please type a number!!')
        wrong_choice()


def main():
    global my_number
    random_number = random.randrange(1, 30)
    my_number=0
    count = 0
    while True:
        wrong_choice()
        if my_number > random_number:
            print("Too high")
        elif my_number < random_number:
            print("Too low")
        else:
            print("Yes!!! {} is my secret number! Congratulation!!!".format
            (my_number))
            input('Press any key to exit program')
            break


if __name__ == '__main__':
    main()
