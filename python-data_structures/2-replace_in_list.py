#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    # Check if the index is negative or out of range
    if idx < 0 or idx >= len(my_list):
        return my_list
    
    # Replace the element at the specified index
    my_list[idx] = element
    return my_list  

# Example usage
if __name__ == "__main__":
    my_list = [10, 20, 30, 40, 50]
    print(replace_in_list(my_list, 2, 99))  
