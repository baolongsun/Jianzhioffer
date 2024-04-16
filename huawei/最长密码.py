def longestPD(input_str):
    set_index = set()
    for i in input_str:
        set_index.add(i)
    best_res = ''
    for j in input_str:
        if j[:-1] in set_index:
            if len(j) > len(best_res):
                best_res = j
    return best_res
if __name__ == "__main__":
    input_str = ['h','he','hel','hell','hello','hellohe']
    print(longestPD(input_str))