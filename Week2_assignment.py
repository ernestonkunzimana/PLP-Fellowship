# 1. to create an empty list called my_list
my_list = []

# 2. And now i have to append the following elements to my_list: 10, 20, 30, 40 as descricribed 
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("After appending:", my_list)  # [10, 20, 30, 40]

# 3. Then insert the value 15 at the second position in the list
my_list.insert(1, 15)
print("After inserting 15:", my_list)  # [10, 15, 20, 30, 40]

# 4. After all the above, let me extend my_list with another list: [50, 60, 70]
my_list.extend([50, 60, 70])
print("After extending:", my_list)  # [10, 15, 20, 30, 40, 50, 60, 70]

# 5. Now it is time to popping up or remove some or the last element from my_list
my_list.pop()
print("After removing last element:", my_list)  # [10, 15, 20, 30, 40, 50, 60]

# 6. Sort my_list in ascending order
my_list.sort()
print("After sorting:", my_list)  # [10, 15, 20, 30, 40, 50, 60]

# 7. Find and print the index of the value 30 in my_list
index_of_30 = my_list.index(30)
print(f"The index of 30 in my_list is: {index_of_30}")  # 3