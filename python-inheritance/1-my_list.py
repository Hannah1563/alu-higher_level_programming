class MyList(list):
    """
    A class that inherits from list and adds a method to print the list sorted.
    """

    def print_sorted(self):
        """
        Prints the elements of the list in ascending order, without modifying the original list.
        """
        # Create a new sorted list (without modifying the original list)
        sorted_list = sorted(self)
        print(sorted_list)
