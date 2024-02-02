import unittest
import random

def bubble_sort(arr):
    # Optimizaiton: if the input array is equal to a sorted array return the array early
    if (arr == sorted(arr)): return arr
    swapped = True
    # swapped will be false if no swaps are made during a pass, indicating the array is sorted
    while(swapped):
        swapped = False
        # set upper bounds to arr.length-1 to compare against right neighbor
        for i in range(0, len(arr) - 1):
            # If the current element is greater than the right neighbor: swap
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
                swapped = True
    return arr

class TestSelectionSort(unittest.TestCase):
    def test_descending(self):
        arr = [9,8,7,6,5,4,3,2,1]
        self.assertEqual(bubble_sort(arr), sorted(arr))

    def test_ascending(self):
        arr = [1,2,3,4,5,6,7,8,9,10]
        self.assertEqual(bubble_sort(arr), arr)

    def test_randomly_generated(self):
        upper_bound = 100
        arr = [random.randint(1, upper_bound) for _ in range(upper_bound)]
        self.assertEqual(bubble_sort(arr), sorted(arr))

    def test_all_elements_same(self):
        arr = [1,1,1,1,1,1,1,1,1,1,1]
        self.assertEqual(bubble_sort(arr), sorted(arr))
        
    def test_empty_array(self):
        arr = []
        self.assertEqual(bubble_sort(arr), [])

    def test_one_element(self):
        arr = [1]
        self.assertEqual(bubble_sort(arr), [1])
    
    def test_all_same_but_one(self):
        arr = [1,1,999,1,1,1,1,1,1,1,1,1,1]
        self.assertEqual(bubble_sort(arr), sorted(arr))

    def test_negative_numbers(self):
        arr = [-3,-5,-38,-9,-122,-30,-1,0]
        self.assertEqual(bubble_sort(arr), sorted(arr))
    pass

if __name__ == '__main__':
    unittest.main()