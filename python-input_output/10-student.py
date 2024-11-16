#!/usr/bin/python3
"""Task 10 """


class Student:
    """
    Represents a student with first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance.
        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of the Student instance.
        If attrs is a list of strings, only the attributes in attrs
        will be included in the returned dictionary.
        Args:
            attrs (list, optional): A list of attribute names to include.
        Returns:
            dict: A dictionary containing the student's attributes.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {key: value for key, value in self.__dict__.items()
                    if key in attrs}
