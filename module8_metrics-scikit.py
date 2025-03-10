import numpy as np
from sklearn.metrics import precision_score, recall_score

def main():
    # Ask the user for input N (positive integer)
    N = int(input("Enter the number of points (N): "))

    # Initialize empty lists to store ground truth (X) and predicted (Y) labels
    X = []
    Y = []

    # Read N (x, y) points from the user
    for i in range(N):
        x = int(input(f"Enter x (ground truth) for point {i+1} (0 or 1): "))
        y = int(input(f"Enter y (predicted) for point {i+1} (0 or 1): "))
        X.append(x)
        Y.append(y)

    # Convert lists to numpy arrays
    X = np.array(X)
    Y = np.array(Y)

    # Compute Precision and Recall using scikit-learn
    precision = precision_score(X, Y)
    recall = recall_score(X, Y)

    # Output the results
    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")

if __name__ == "__main__":
    main()
