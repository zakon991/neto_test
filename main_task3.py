def discriminant(a, b, c):

    return b ** 2 - 4 * a * c


def solution(a, b, c):

    if discriminant(a, b, c) < 0:
        print('корней нет')
    elif discriminant(a, b, c) == 0:
        print((-b) / (2 * a))
    elif discriminant(a, b, c) > 0:
        print((-b + discriminant(a, b, c) ** (0.5)) / 2 * a, (-b - discriminant(a, b, c) ** (0.5)) / 2 * a)


if __name__ == '__main__':
    solution(1, 8, 15)
    solution(1, -13, 12)
    solution(-4, 28, -49)
    solution(1, 1, 1)