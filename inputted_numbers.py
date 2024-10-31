# Variables/Counters for each range
count_1_10 = 0
count_11_20 = 0
count_21_30 = 0
count_31_40 = 0
count_41_50 = 0

def is_valid_number(number):
    # Checks if the the number inputted is between 1 and 50
    return number.isdigit() and 1 <= int(number) <= 50

numbers = []

while True:
    number = input("Input a number between 1 and 50: ")
    if not is_valid_number(number):
        print("Error! Invalid number given. Please enter a valid number")
        break

    # Converts numbers into integers and adds them to the list
    number = int(number)
    numbers.append(number)

    # Range counter
    if 1 <= number <= 10:
        count_1_10 += 1
    elif 11 <= number <= 20:
        count_11_20 += 1
    elif 21 <= number <= 30:
        count_21_30 += 1
    elif 31 <= number <= 40:
        count_31_40 += 1
    elif 41 <= number <= 50:
        count_41_50 += 1

# Displays the results for each range
print("\nNumber of inputs in each range:")
print(f"1 - 10 = {count_1_10}")
print(f"11 - 20 = {count_11_20}")
print(f"21 - 30 = {count_21_30}")
print(f"31 - 40 = {count_31_40}")
print(f"41 - 50 = {count_41_50}")