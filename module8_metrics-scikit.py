import numpy as np
from sklearn.metrics import precision_score, recall_score


def readData():
    numPoints = int(input("Enter N (positive integer): "))
    xTrue = np.zeros(numPoints, dtype=int)
    yPred = np.zeros(numPoints, dtype=int)
    for i in range(numPoints):
        print(f"Point {i + 1}:")
        xVal = int(input("  Enter x (true label, 0 or 1): "))
        yVal = int(input("  Enter y (predicted label, 0 or 1): "))
        xTrue[i] = xVal
        yPred[i] = yVal
    return xTrue, yPred


def computeMetrics(xTrue, yPred):
    precisionValue = precision_score(xTrue, yPred, pos_label=1, zero_division=0)
    recallValue = recall_score(xTrue, yPred, pos_label=1, zero_division=0)
    return precisionValue, recallValue


def main():
    xTrue, yPred = readData()
    precisionValue, recallValue = computeMetrics(xTrue, yPred)
    print(f"Precision = {precisionValue:.2f}")
    print(f"Recall    = {recallValue:.2f}")


if __name__ == "__main__":
    main()
