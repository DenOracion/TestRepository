numbers = [10, 20, 30, 40, 50] #ask the list to print both 10 and 50
print("First Element:", numbers[0])
print("Last Element:", numbers[-1])

# Replacing elements in lists
animals = ["cat", "dog", "bird"]
animals[1] = "hamster"
print(animals)

# Appending and removing elements using .append and .remove function
colors = []
colors.append("red")
colors.append("green")
colors.append("blue")
colors.remove("green")
print(colors)

#Finding the length of a list
names = ["Alice", "Bob", "Charlie", "Diana"]
print("Length of the list:", len(names))

# Finding the sum of all the numbers in a list
number = [4, 7, 1, 8, 5]
total_sum = sum(number)
print("Sum of elements:", total_sum)

# minmaxxing or finding minimum and maximum element values
ages = [23, 45, 18, 34, 60]
print("Maximum age:", max(ages))
print("Mininmum age:", min(ages))

# Sorting a list in ascending order using .sort function
scores = [88, 56, 92, 78, 61]
scores.sort()
print("Sorted list:", scores)

# Checking if a value exists in a list with if else
number_1 = [1, 3, 5, 7, 9]
if 5 in number_1:
    print("Found")
else:
    print("Not Found")

# Counting occurences of an element; or counting how many times a value appears in a list
items = [1, 2, 2, 3, 4, 4, 4, 5]
count_of_4 = items.count(4) #using .count function
print("Count of 4:", count_of_4)

#activity: combining lists with .extend function
list1 = [17, 9, 21, 25, 18]
list2 = [10, 6, 14]
list1.extend(list2)
print(list1)

# Reverse function
list3 = [6, 9, 7, 4, 17, 12, 15, 3]
list3.reverse()
print(list3)