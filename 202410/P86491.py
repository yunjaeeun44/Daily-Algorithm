def solution(sizes):
    for size in sizes:
        size.sort(reverse=True)
    a = max(size[0] for size in sizes)
    b = max(size[1] for size in sizes)
    return a*b