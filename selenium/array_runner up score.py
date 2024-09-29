if __name__ == '__main__':
    input_str = input().split()
    arr = list(map(int, input_str))

    arr.sort()
    print(arr)

    n = len(arr)
    print(arr[n-2])
