def get_parent(height, root, flux_converter):
    if root == flux_converter:
        return -1

    right = root - 1
    if flux_converter == right:
        return root

    height -= 1
    left = root - (2 ** height)
    if flux_converter == left:
        return root

    # print(root, left, right)
    return get_parent(height, left, flux_converter) if flux_converter < left \
                                                    else get_parent(height, right, flux_converter)


def solution(h, q):
    root = 2**h - 1
    r = []
    for i in q:
        p = get_parent(h, root, i)
        r.append(p)

    return r

print(solution(5, [19, 14, 28]))
print(solution(3, [7, 3, 5, 1]))
