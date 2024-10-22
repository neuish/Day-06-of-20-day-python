#list compherension
#1. print squares in a list
squares = [values**2 for values in range (1, 11)]
print(squares)

#2. counting 1-20
count = []
for numbers in range (1, 21):
    count.append(numbers)

print(count)

#3. million list
thousand_numbers = []
for numbers in range (1, 1001):
    thousand_numbers.append(numbers)
print(thousand_numbers)

#4. million min max sum

# Create a list of numbers from 1 to 1,000,000
million_numbers = list(range(1, 1000001))

# Check minimum and maximum
print("Min value starts at:", min(million_numbers))  # Should print 1
print("Max value ends at:", max(million_numbers))    # Should print 1,000,000

# Calculate the sum
total = sum(million_numbers)
print("Sum of the list:", total)


#5. off numvers
numbers = []
for number in range (1, 21):
    if number % 2 == 1:
        numbers.append(number)
print(numbers)


#6. multiplication
numbers = []
for number in range (3, 31):
    if number % 3 == 0:
        numbers.append(number)
print(numbers)


#7. cube
cube = [pow(numbers, 3) for numbers in range(1, 11)]
print(cube)