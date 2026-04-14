#https://github.com/saadkhan17406-sketch/Python
print ("UIN : 251A053")
import numpy as np

arr1 = np.array([1, 2, 3, 4, 5, 6])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
arr3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

print("2D Array:\n", arr2)

reshaped = arr1.reshape(2, 3)
print("\nReshaped Array (2x3):\n", reshaped)

print("\nSlicing (First row of 2D array):", arr2[0, :])

print("\nIndexing (Element at [1, 1]):", arr2[1, 1])

print("\n3D Array:\n", arr3)