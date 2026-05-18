import numpy as np

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return np.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)  # Euclidean distance


def knn_regression(points, k, x_query):
    """
    Performs k-NN regression.

    Args:
        points: A list of Point objects.
        k: The number of nearest neighbors to consider.
        x_query: The x-coordinate of the query point.

    Returns:
        The predicted y-value for the query point, or an error message if k > N.
    """

    if k > len(points):
        return "Error: k cannot be greater than the number of data points."

    # Calculate distances to the query point
    distances = [p.distance(Point(x_query, 0)) for p in points]  # Create a dummy Point for x_query

    # Get the indices of the k nearest neighbors
    nearest_indices = np.argsort(distances)[:k]

    # Calculate the average y-value of the k nearest neighbors
    y_values = [points[i].y for i in nearest_indices]
    predicted_y = np.mean(y_values)

    return predicted_y


if __name__ == "__main__":
    # Get input N
    N = int(input("Enter the number of data points (N): "))

    # Get input k
    k = int(input("Enter the number of neighbors (k): "))

    # Read data points
    points = []
    for i in range(N):
        x = float(input(f"Enter x-coordinate for point {i+1}: "))
        y = float(input(f"Enter y-coordinate for point {i+1}: "))
        points.append(Point(x, y))

    # Get query point x
    x_query = float(input("Enter the x-coordinate of the query point (X): "))

    # Perform k-NN regression
    result = knn_regression(points, k, x_query)

    # Print the result
    print("Result (Y):", result)