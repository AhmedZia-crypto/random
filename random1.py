import random
a = random.randint(1,20)

while True:
    g = int(input("Enter the number you guessed (1, 20) :"))
   
    if a==g:
        print("You guessed the number right !")
        break
    else:
        print("You guessed the number wrong ")
        