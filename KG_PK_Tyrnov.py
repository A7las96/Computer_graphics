import math
import numpy as np

#  прошу прощения что передаю в функции переменные не в том виде,
#  что вы указали, посчитал такой вариант более многофункциональным


def rotation(x, y, alpha):
    #  p' = M_x_y(R_alpha(M_-x_-y * p))
    rot_matrix = np.array([[math.cos(alpha), math.sin(-1 * alpha), 0], [math.sin(alpha), math.cos(alpha), 0], [0, 0, 1]])
    matrix_positive = np.array([[1, 0, x], [0, 1, y], [0, 0, 1]])
    matrix_negative = np.array([[1, 0, -1 * x], [0, 1, -1 * y], [0, 0, 1]])
    p = matrix_positive.dot(rot_matrix)
    p = p.dot(matrix_negative)
    return p


def get_normal(point_A: list, point_B: list, point_C: list):
    """
    :param point_A: координаты точки А
    :param point_B: координаты точки B
    :param point_C: координаты точки C
    :return: координаты нормали
    """

    n_y: int = (point_B[2] - point_A[2]) * (point_C[0] - point_A[0]) - (point_C[2] - point_A[2]) * (
            point_B[0] - point_A[0])
    n_z: int = -((point_B[1] - point_A[1]) * (point_C[0] - point_A[0]) - (point_C[1] - point_A[1]) * (
            point_B[0] - point_A[0]))

    n_x: int = -(n_z * (point_B[2] - point_A[2]) + n_y * (point_B[1] - point_A[1])) / (point_B[0] - point_A[0])

    gcd = math.gcd(int(n_x), int(n_y))  # кратно уменьшим координаты

    gcd = math.gcd(gcd, int(n_z))

    return n_x / gcd, n_y / gcd, n_z / gcd


def belongs_projection(point_A: list, point_B: list, point_C: list, point_O: list):
    """
    :param point_A: координаты точки А
    :param point_B: координаты точки B
    :param point_C: координаты точки C
    :param point_O: координаты точки, для которой определяется принадлежность
    """

    check_1 = (point_A[0] - point_O[0]) * (point_B[1] - point_A[1]) - \
              (point_B[0] - point_A[0]) * (point_A[1] - point_O[1])

    check_2 = (point_B[0] - point_O[0]) * (point_C[1] - point_B[1]) - \
              (point_C[0] - point_B[0]) * (point_B[1] - point_O[1])

    check_3 = (point_C[0] - point_O[0]) * (point_A[1] - point_C[1]) - \
              (point_A[0] - point_C[0]) * (point_C[1] - point_O[1])

    belongs: bool = (check_1 < 0 and check_2 < 0 and check_3 < 0) or (check_1 > 0 and check_2 > 0 and check_3 > 0)

    if belongs:
        print('Точка принадлежит проекции')
    else:
        print('Точка не принадлежит проекции')


if __name__ == '__main__':

    print('Задание 1:')
    print(rotation(5, 5, 0.35))
    print()

    print('Задание 2:')
    A = [20, 20, 30]
    B = [45, 75, 80]
    C = [120, 80, 55]
    print(get_normal(A, B, C))
    print()

    print('Задание 3:')
    A = [20, 20, 20]
    B = [60, 50, 75]
    C = [30, 120, 100]
    does_belong = [30, 30]
    belongs_projection(A, B, C, does_belong)
