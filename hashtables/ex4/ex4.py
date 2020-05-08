def has_negatives(a):
    result = []
    neg_dict = {}
    pos_dict = {}

    for i in a:
        if i < 0:
            neg_dict[i] = i*-1
        else:
            pos_dict[i] = i

    for neg_inverse in neg_dict.values():
        if neg_inverse in pos_dict:
            result.append(pos_dict[neg_inverse])

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
