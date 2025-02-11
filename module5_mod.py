class NumberList:
    def __init__(self):
        self.numbers = []

    def insert_numbers(self, n):
        """
        Inserts N numbers into the list by asking the user for each number.
        """
        for i in range(n):
            num = int(input(f"Enter number {i+1}: "))
            self.numbers.append(num)

    def find_number(self, x):
        """
        Finds the index of the number X in the list. Returns -1 if not found.
        """
        if x in self.numbers:
            return self.numbers.index(x) + 1  # Add 1 to return 1-based index
        return -1
