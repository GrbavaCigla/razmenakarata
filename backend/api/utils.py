from typing import List


def split_list(text: List[str], delims: List[str]):
    prev = 0
    ind = 0
    res = []

    for i, j in enumerate(text):
        if ind == len(delims):
            break

        if j == delims[ind]:
            res.append(text[prev:i])
            ind += 1
            prev = i + 1

    return res
