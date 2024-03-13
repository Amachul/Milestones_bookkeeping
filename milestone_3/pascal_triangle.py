def next_row(src):
    res = []
    i = 0
    while i < len(src):
        res.append(src[i]) if i == 0 else res.append(src[i - 1] + src[i])
        i += 1
    res.append(1)
    return res


def get_triangle(rows: int) -> list[list[int]]:
    triangle = [[1]]
    for i in range(rows_amount - 1):
        triangle.append(next_row(triangle[i]))
    return triangle


def print_triangle(triangle_):
    for i in triangle_:
        print(str(i).center(len(str(triangle_[len(triangle_) - 1]))))


rows_amount = int(input("Enter amount of rows to print"))
triangle = get_triangle(rows_amount)
print_triangle(triangle)
