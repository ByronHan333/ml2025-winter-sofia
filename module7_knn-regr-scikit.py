import numpy as np
from sklearn.neighbors import KNeighborsRegressor

def main():
    # Read N
    while True:
        try:
            N = int(input("Enter N (positive integer): "))
            if N > 0:
                break
            print("Error: N must be positive.")
        except ValueError:
            print("Error: Please enter an integer.")

    # Read k
    while True:
        try:
            k = int(input(f"Enter k (positive integer <= {N}): "))
            if k > 0:
                if k <= N:
                    break
                print(f"Error: k must be <= {N}.")
            else:
                print("Error: k must be positive.")
        except ValueError:
            print("Error: Please enter an integer.")

    # Read N points
    X_train = []
    y_train = []
    for i in range(N):
        while True:
            try:
                x = float(input(f"Enter x value for point {i+1}: "))
                y = float(input(f"Enter y value for point {i+1}: "))
                X_train.append(x)
                y_train.append(y)
                break
            except ValueError:
                print("Error: Please enter valid real numbers.")

    # Convert to numpy arrays and reshape for sklearn
    X_train = np.array(X_train).reshape(-1, 1)
    y_train = np.array(y_train)

    # Read X for prediction
    while True:
        try:
            X = float(input("Enter X for prediction: "))
            break
        except ValueError:
            print("Error: Please enter a valid real number.")

    # Train k-NN regressor
    model = KNeighborsRegressor(n_neighbors=k)
    model.fit(X_train, y_train)

    # Predict
    y_pred = model.predict([[X]])

    # Calculate variance
    variance = np.var(y_train, ddof=0)

    # Output results
    print(f"\nPredicted Y: {y_pred[0]:.4f}")
    print(f"Variance of training labels: {variance:.4f}")

if __name__ == "__main__":
    main()
