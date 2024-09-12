numbers = []
while True:
    add_number = input("Would you like to add a number, y or n: ")
    if add_number == 'y':
        number = float(input("Enter a number: "))
        numbers.append(number)
    else:
        average = sum(numbers)/len(numbers)
        print(f"The average of the numbers entered is {average}")
        break
