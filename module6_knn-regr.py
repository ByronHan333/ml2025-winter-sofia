import numpy as np

class KNNRegressor:
    def __init__(self, k):
        self.k = k
        self.points = None

    def fit(self, X, Y):
        self.points = np.column_stack((X, Y))

    def predict(self, X_query):
        if self.points is None:
            raise ValueError("Model has not been fitted with data.")

        distances = np.abs(self.points[:, 0] - X_query)
        k_nearest_indices = np.argsort(distances)[:self.k]
        k_nearest_values = self.points[k_nearest_indices, 1]

        return np.mean(k_nearest_values)

# User Input
N = int(input("Enter N (number of points): "))
k = int(input("Enter k (number of nearest neighbors): "))

if k > N:
    print("Error: k cannot be greater than N.")
else:
    X_values = []
    Y_values = []

    for i in range(N):
        x = float(input(f"Enter x{i+1}: "))
        y = float(input(f"Enter y{i+1}: "))
        X_values.append(x)
        Y_values.append(y)

    X_values = np.array(X_values)
    Y_values = np.array(Y_values)

    model = KNNRegressor(k)
    model.fit(X_values, Y_values)

    X_query = float(input("Enter X to predict Y: "))
    result = model.predict(X_query)
    print(f"Predicted Y: {result}")
