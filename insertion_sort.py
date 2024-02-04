import unittest
import random
import time

def insertion_sort(arr):
    for i in range(len(arr)):
        curr = arr[i]
        j = i
        while j > 0 and arr[j-1] > curr:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = curr
    return arr

class TestInsertionSort(unittest.TestCase):
    def test_small_array(self):
        arr = [2, 1]
        self.assertEqual(insertion_sort(arr), sorted(arr))

    def test_large_array(self):
        upper_bound = 10
        arr = [random.randint(1, upper_bound) for _ in range(upper_bound)]
        self.assertEqual(insertion_sort(arr), sorted(arr))

    def test_nearly_sorted(self):
        arr = [1,2,3,4,5,6,7,9,8,10]
        self.assertEqual(insertion_sort(arr), sorted(arr))

    def test_reversed(self):
        start_time = time.time_ns()
        start_value = 10000
        arr = [start_value - i for i in range(start_value)]
        result = insertion_sort(arr)
        print("test_reversed took", "{:.2f}".format((time.time_ns() - start_time) / 1000000000), "seconds to complete")
        self.assertEqual(result, sorted(arr))
    
    def test_stability(self):
        obj = [
            (150,'a'),
            (11,'b'),
            (4,'c'),
            (3,'d'),
            (6,'these'),
            (6,'are'),
            (6,'in'),
            (6,'the'),
            (6,'same'),
            (6,'order'),
            (8,'e'),
            (19,'f'),
            (2,'g'),
            (100,'h'),
        ]
        keys = [i[0] for i in obj]
        result = insertion_sort_stability(obj)
        result_keys = [i[0] for i in result]
        for r in result:
            print(r)
        self.assertEqual(result_keys, sorted(keys))

# Because I'm passing in an array of tuples now,
# I had to change how I index the input array
def insertion_sort_stability(arr):
    for i in range(len(arr)):
        curr = arr[i]
        j = i
        while j > 0 and arr[j-1][0] > curr[0]:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = curr
    return arr   

if __name__ == '__main__':
    unittest.main()