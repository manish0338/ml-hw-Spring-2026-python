import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


def read_dataset(num_pairs):
    X = np.empty((num_pairs, 1), dtype=float)
    y = np.empty(num_pairs, dtype=int)

    for i in range(num_pairs):
        x_val = float(input(f"  Enter x value for pair {i + 1}: "))
        y_val = int(input(f"  Enter y value for pair {i + 1}: "))
        X[i, 0] = x_val
        y[i] = y_val

    return X, y


def main():
    N = int(input("Enter N (number of training pairs): "))
    print("Enter the training pairs:")
    X_train, y_train = read_dataset(N)

    M = int(input("Enter M (number of test pairs): "))
    print("Enter the test pairs:")
    X_test, y_test = read_dataset(M)

    best_k = None
    best_accuracy = -1.0

    max_k = min(10, N)

    for k in range(1, max_k + 1):
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(X_train, y_train)
        y_pred = knn.predict(X_test)
        acc = accuracy_score(y_test, y_pred)

        if acc > best_accuracy:
            best_accuracy = acc
            best_k = k

    print(f"\nBest k: {best_k}")
    print(f"Test accuracy: {best_accuracy:.4f}")


if __name__ == "__main__":
    main()
