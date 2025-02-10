# Ask the user to input N (positive integer)
N = int(input("Enter a positive integer N: "))

# Initialize an empty list to store N numbers
numbers = []

# Read N numbers one by one
print(f"Enter {N} numbers:")
for i in range(N):
    number = int(input(f"Number {i + 1}: "))
    numbers.append(number)

# Ask the user to input X (integer)
X = int(input("Enter an integer X: "))

# Check if X is in the list of N numbers
if X in numbers:
    index = numbers.index(X) + 1  # Add 1 to convert 0-based index to 1-based
    print(f"Index of X: {index}")
else:
    print("-1")
