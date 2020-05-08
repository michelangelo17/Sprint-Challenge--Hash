def get_indices_of_item_weights(weights, length, limit):
    weights_dict = {}

    for i, w in enumerate(weights):
        if w in weights_dict:
            weights_dict[w].append(i)
        else:
            weights_dict[w] = [i]

    for i, w in enumerate(weights_dict):
        if limit-w in weights_dict:
            if weights_dict[limit-w] is weights_dict[w]:
                if len(weights_dict[w]) >= 2:
                    return (weights_dict[limit-w][1], weights_dict[w][0])
            else:
                return (weights_dict[limit-w][0], weights_dict[w][0])

    return None
