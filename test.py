import numpy as np

list_1 = [[1,2,3], [4,5,6]]
arr_1 = np.array(list_1)
print(np.stack(arr_1, 0))