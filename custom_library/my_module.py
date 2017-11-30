"""
All the fancy stuff that my library is going to do
"""

class Adder:
    """Definition for a line"""
    def __init__(self, number):
        self.number = number

    def add_one(self):
        """Add 1 to number attribute"""
        self.number += 1
        return self.number

    def add_two(self): 
        """Adds 2 to number attribute"""
        self.number += 2
        return self.number
