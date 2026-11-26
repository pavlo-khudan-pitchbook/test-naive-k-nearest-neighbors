from distance import euclidean_distance

# 2) Utilizing Euclidean distance as our distance metric, write a function to calculate the K-Nearest Neighbors (KNN) of
#    our data set given an input `query_array: list[list[float]]` and `k: int`, dataset: list[list[float]]. 
#    Return a "list of lists of the point indexes, list[list[int]]" of the K nearest neighbors, in order (starting from closest).

def naive_knn(query_array: list[list[float]], dataset: list[list[float]], k=10) -> list[list[int]]:
    """Naive K-nearest neighbors implementation."""
    pass

dataset = [
     [10, 11, 12],
     [1, 2, 3],
     [4, 5, 6],
     [7, 8, 9],
     [13, 14, 15]
   ]
queries = [
   [4, 5, 6],
   [9, 10, 11],
   [4, 2, 4]
]

if __name__ == "__main__":
    results = naive_knn(queries, dataset, k=3)
    for q, result in zip(queries, results):
       print(f"Query vector: {q}")
       for r in result:
          print(f"\tResult i: {r}, vector: {dataset[r]}")