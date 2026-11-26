from math import sqrt

# 1) Write a function that computes the Euclidean distance
#    between two points in n-dimensional space.

#    The function should:
#    - Accept two points as input, where each point is represented as a list/array of coordinates.
#    - Handle points of arbitrary dimensions (both points must have same dimensions).
#    - Return the Euclidean distance as a float.
#    - Return ValueError if spaces do not match
#    Examples:
#    Distance between [1, 2] and [4, 6] in 2D space
#    Distance between [1, 2, 3] and [4, 5, 6] in 3D space

def euclidean_distance(a: list[float], b: list[float]) -> float:
  """Multi-dimensional Euclidean distance metric."""
  if len(a) != len(b):
      raise ValueError()
  square_diffs = [(b[i] - a[i]) ** 2 for i in range(len(a))]
  return sqrt(sum(square_diffs))

dataset = [
     [10, 11, 12],
     [1, 2, 3],
     [4, 5, 6],
     [7, 8, 9],
     [13, 14, 15]
   ]
failing_dataset = [
     [10, 11, 12],
     [1, 2],
     [4, 5, 6, 2]
]

if __name__ == "__main__":
    for i in range(1, len(dataset)):
        print(euclidean_distance(dataset[0], dataset[i]))

    for i in range(1, len(failing_dataset)):
        try:
            euclidean_distance(failing_dataset[0], failing_dataset[i])
        except ValueError:
            print(f"Successful error!")