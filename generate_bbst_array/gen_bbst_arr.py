def GenerateBBSTArray(a):
    def middle_element_left_right_array(arr):
        start = 0
        stop = len(arr)
        index = int((stop - start) / 2)
        left = arr[start: index]
        right = arr[index + 1:]
        return arr[index], left, right

    if len(a) == 0:
        return a

    input_arr = sorted(a)
    queue = [input_arr]
    output = [None]*len(input_arr)
    counter = 0
    while len(queue) > 0:
        next_level = []
        for q in queue:
            elem, left, right = middle_element_left_right_array(q)
            output[counter] = elem
            counter += 1
            if len(left) > 0:
                next_level.append(left)
            if len(right) > 0:
                next_level.append(right)
        queue = next_level
    return output
