#Collatz sequence
def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1

while True:
    try:
        guess = int(input("Enter number:"))
    except ValueError:
        print("Please enter a number!")
    while guess > 1:
        guess = collatz(guess)
    #break #Ends infinite loop of Collatz sequences
