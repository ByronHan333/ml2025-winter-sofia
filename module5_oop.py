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


def main():
    # Ask user for input N (positive integer)
    n = int(input("Enter the number of elements (N): "))

    # Create an object of NumberList
    number_list = NumberList()

    # Insert N numbers into the list
    number_list.insert_numbers(n)

    # Ask user for input X (integer)
    x = int(input("Enter the number (X) to find: "))

    # Find the index of X and print the result
    result = number_list.find_number(x)
    if result == -1:
        print("-1")  # X not found
    else:
        print(f"The number {x} is found at index {result}.")

if __name__ == "__main__":
    main()
