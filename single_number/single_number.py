'''

'''


def single_number(arr):
    # Your code here
    if len(arr) == 1:
        return arr[0]
    else:
        for num in arr:
            if arr.count(num) == 1:
                return num


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
