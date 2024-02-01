import unittest
import random

def selection_sort(arr):
    for i in range(len(arr)):
        max = i
        for j in range(i + 1, len(arr)):
            if arr[j] > arr[max]:
                max = j
        temp = arr[max]
        arr[max] = arr[i]
        arr[i] = temp
    return arr

class TestSelectionSort(unittest.TestCase):
    def test_descending(self):
        arr = [9,8,7,6,5,4,3,2,1]
        self.assertEqual(selection_sort(arr), sorted(arr, reverse=True))

    def test_ascending(self):
        arr = [1,2,3,4,5,6,7,8,9,10]
        self.assertEqual(selection_sort(arr), arr)

    def test_randomly_generated(self):
        upper_bound = 100
        arr = [random.randint(1, upper_bound) for _ in range(upper_bound)]
        self.assertEqual(selection_sort(arr), sorted(arr, reverse=True))

    def test_all_elements_same(self):
        arr = [1,1,1,1,1,1,1,1,1,1,1]
        self.assertEqual(selection_sort(arr), sorted(arr, reverse=True))
        
    def test_empty_array(self):
        arr = []
        self.assertEqual(selection_sort(arr), [])

    def test_one_element(self):
        arr = [1]
        self.assertEqual(selection_sort(arr), [1])
    
    def test_all_same_but_one(self):
        arr = [1,1,999,1,1,1,1,1,1,1,1,1,1]
        self.assertEqual(selection_sort(arr), sorted(arr, reverse=True))

    def test_negative_numbers(self):
        arr = [-3,-5,-38,-9,-122,-30,-1,0]
        self.assertEqual(selection_sort(arr), sorted(arr, reverse=True))
if __name__ == '__main__':
    unittest.main()