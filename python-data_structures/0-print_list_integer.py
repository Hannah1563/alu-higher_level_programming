#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for number in my_list:
        print("{}".format(number))

# Example usage
if __name__ == "__main__":
    print_list_integer([1, 2, 3, 4, 5])
    print_list_integer([-1, 0, 100, 99])