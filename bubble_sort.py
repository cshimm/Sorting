import unittest

def bubble_sort(arr):
    swapped = True
    count = 0
    while(swapped):
        swapped = False
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
                swapped = True
                count += 1
    return arr

class TestSelectionSort(unittest.TestCase):
    def test_descending(self):
        arr = [9,8,7,6,5,4,3,2,1,0]
        self.assertEqual(bubble_sort(arr), sorted(arr))
    pass

if __name__ == '__main__':
    unittest.main()