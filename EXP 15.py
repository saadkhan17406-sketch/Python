#https://github.com/saadkhan17406-sketch/Python
print ("UIN : 251A053")
def calculate_average(numbers):
    if len(numbers) == 0:
        return 0  # Handle the case for an empty list
    total = 0
    for num in numbers:
        total += num
    average = total / len(numbers)  # Fixed the syntax for calculating average
    return average

data = [10, 20, 30, 0]
result = calculate_average(data)
print("Average:", result)

empty_data = []
result2 = calculate_average(empty_data)
print("Average of empty list:", result2)