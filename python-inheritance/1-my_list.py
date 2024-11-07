class MyList(list):
         """A list that can print itself in sorted order."""
         
         def print_sorted(self):
             """Print the list in ascending sorted order."""
             print(sorted(self))
