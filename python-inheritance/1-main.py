#!/usr/bin/python3
MyList = __import__('1-my_list').MyList

my_list = MyList()
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)
my_list.append(5)

# Original list print
print(my_list)  # [1, 4, 2, 3, 5]

# Print sorted list (without modifying the original list)
my_list.print_sorted()  # [1, 2, 3, 4, 5]

# Original list is unchanged after print_sorted
print(my_list)  # [1, 4, 2, 3, 5]
