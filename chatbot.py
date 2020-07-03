def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input("Enter for 3: "))
    rem5 = int(input("Enter for 5: "))
    rem7 = int(input("Enter for 7: "))
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():
    print("Let's test your programming knowledge.")
    print("Guess the name of python developer?")
    print("1. Dennis Ritchie!")
    print("2. Bjarne Stroustrup!")
    print("3. Guido van Rossum!")
    print("4. James Gosling!")
    while(1):
        ans=int(input("Choose option 1,2,3,4: "))
        if(ans != 3):
            print("Please, try again.")
        else:
            break
    print('Completed, have a nice day!')


def end():
    print('Congratulations, have a nice day!')


greet('Taker', '2020')
print()
remind_name()
print()
guess_age()
print()
count()
print()
test()
print()
end()