def is_valid_number(number):
    return number.isdigit() and 1 <= int(number) <= 50
while True:
    number = input("Input a number between 1 and 50: ")
    if not is_valid_number(number):
        print("Error! Invalid number given. Please enter a valid number")
        break