def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    total = sum(numbers)
    return total / len(numbers)

my_list = []
result = calculate_average(my_list)
print(f"The average is: {result}")

#Robust solution
def calculate_average_robust(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

my_list = []
result = calculate_average_robust(my_list) 
print(f"The robust average is: {result}") #This will not cause ZeroDivisionError