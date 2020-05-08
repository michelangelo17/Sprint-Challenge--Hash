def intersection(arrays):
    result = []
    arr_dict = {}

    for i in arrays:
        for j in i:
            if j in arr_dict:
                arr_dict[j] += 1
            else:
                arr_dict[j] = 1

    for key in arr_dict.keys():
        if arr_dict[key] == len(arrays):
            result.append(key)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
