from module5_mod import NumberList

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
