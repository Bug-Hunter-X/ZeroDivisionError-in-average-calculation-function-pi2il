def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    total = sum(numbers)
    return total / len(numbers) #this will cause ZeroDivisionError if the list is empty

my_list = []
result = calculate_average(my_list)
print(f"The average is: {result}")