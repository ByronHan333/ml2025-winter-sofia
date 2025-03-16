import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score

def get_input_pairs(num_pairs, dataset_name):
    """Reads num_pairs (x, y) pairs from user input."""
    data = np.zeros((num_pairs, 2))
    print(f"Enter {num_pairs} (x, y) pairs for {dataset_name}:")
    for i in range(num_pairs):
        x = float(input(f"Enter x for pair {i+1}: "))
        y = int(input(f"Enter y for pair {i+1}: "))
        data[i] = [x, y]
    return data

def main():
    # Read training set
    N = int(input("Enter the number of training samples (N): "))
    train_data = get_input_pairs(N, "Training Set")

    # Read test set
    M = int(input("Enter the number of test samples (M): "))
    test_data = get_input_pairs(M, "Test Set")

    # Split features and labels
    X_train, y_train = train_data[:, 0].reshape(-1, 1), train_data[:, 1]
    X_test, y_test = test_data[:, 0].reshape(-1, 1), test_data[:, 1]

    # Define the k range
    param_grid = {'n_neighbors': list(range(1, 11))}  # k in range [1,10]

    # Perform GridSearchCV to find the best k
    knn = KNeighborsClassifier()
    grid_search = GridSearchCV(knn, param_grid, cv=5, scoring='accuracy')
    grid_search.fit(X_train, y_train)

    # Get the best model
    best_k = grid_search.best_params_['n_neighbors']
    best_model = grid_search.best_estimator_

    # Evaluate on test data
    y_pred = best_model.predict(X_test)
    test_accuracy = accuracy_score(y_test, y_pred)

    # Output results
    print(f"Best k: {best_k}")
    print(f"Test Accuracy: {test_accuracy:.4f}")

if __name__ == "__main__":
    main()
