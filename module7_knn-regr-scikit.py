import numpy as np
from sklearn.neighbors import KNeighborsRegressor

# Read N (positive integer)
N = int(input("Enter N (number of points): "))

# Read k (positive integer)
k = int(input("Enter k (number of neighbors): "))

# Initialize numpy arrays for data
X_data = np.empty((N, 1), dtype=float)
y_data = np.empty(N, dtype=float)

# Read N (x, y) points one by one
for i in range(N):
    x_val = float(input(f"Enter x for point {i+1}: "))
    y_val = float(input(f"Enter y for point {i+1}: "))
    X_data[i, 0] = x_val
    y_data[i] = y_val

# Read query X
X_query = float(input("Enter X for prediction: "))

# Perform k-NN Regression if k <= N, else error
if k > N:
    print("Error: k must be less than or equal to N")
else:
    knn = KNeighborsRegressor(n_neighbors=k)
    knn.fit(X_data, y_data)
    prediction = knn.predict(np.array([[X_query]]))
    print(f"k-NN Regression result (Y): {prediction[0]}")

# Variance of labels in training dataset
variance = np.var(y_data)
print(f"Variance of labels: {variance}")
