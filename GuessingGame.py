import random

print("Hey welcome to my world, Guess the right number and your life will be changed!")



while True:
    random_ = random.randint(1, 100)
    input_ = int(input("Write your number here: "))
    difference = abs(100 - input_)
    
    if difference == 0:
        print("Great! You have found the number!")
        break
    elif 0 < difference <= 2:
        print("Very Hot!")
    elif 3 <= difference <= 20:
        print("Hot")
    elif 21 <= difference <= 60:
        print("Cold")
    elif 61 <= difference < 100:
        print("Very Cold")
    elif difference >= 100:
        print("it's cold for polar bear")
        




