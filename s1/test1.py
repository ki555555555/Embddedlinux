def count_4_in_list(input_list):
    count = 0
    for num in input_list:
        count += str(num).count('4')
    return count

# Example list
numbers = [14, 24, 34, 45, 48, 54, 64]

# Count the occurrences of 4
result = count_4_in_list(numbers)
print(f"The number 4 appears {result} times in the list.")
