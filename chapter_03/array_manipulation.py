numbers = [2, 2, 3]
# change value in a list
numbers[0] = 1
print(numbers)

numbers.append(5)
print(numbers)

numbers.insert(-1, 4)
print(numbers)

# remove elements from a list python
del numbers[0]
print(numbers)

removed_number = numbers.pop()
print(removed_number)

abc = ["a", "b", "c"]
abc.remove("b")
print(removed_number)
