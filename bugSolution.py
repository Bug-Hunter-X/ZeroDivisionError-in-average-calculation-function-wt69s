def calculate_average(numbers):
    if not numbers:
        return None  # Return None for an empty list
    total = sum(numbers)
    average = total / len(numbers)
    return average

my_list = []
result = calculate_average(my_list)
print(f"Average: {result}") # Output: Average: None

my_list = [10,20,30]
result = calculate_average(my_list)
print(f"Average: {result}") # Output: Average: 20.0