print(f"provide count of numbers")

# Read N - the count of numbers
N = int(input())

print(f"reading {N} numbers")
# Read N numbers one by one
numbers = []
for i in range(N):
    print(f"entery {i+1} number")
    num = int(input())
    numbers.append(num)

print(f"enter number to search for")
# Read X - the number to search for
X = int(input())

# Search for X in the list
result = -1
for i in range(N):
    if numbers[i] == X:
        result = i + 1  # Index from 1 to N
        break

if result == -1:
    print("number is not found")
else:
    print("number is found")

print(result)
