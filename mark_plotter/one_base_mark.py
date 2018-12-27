def compute_mark_from_zero_quadratic(value, quadratic_factor=-1, linear_factor=0):
    """
    Use this function to generate a mark for a value which should be zero. At zero, the mark is one. A quadratic penalty
    is applied, The function si symmetric with respect to zero.

    :param value: the value which should be zero
    :param quadratic_factor: the quadratic factor penalty to apply
    :param linear_factor: the linear factor penalty to apply
    :return: the mark for the value, floored to 0
    """
    mark = 1 + quadratic_factor * (value ** 2) + linear_factor * abs(value)
    return max(mark, 0)


def compute_mark_from_zero_linear(value, slope=-1):
    """
    Use this function to generate the mark for a value which has 0 as goal, applying a linear penalty. At value zero,
    the mark is one. The function is symmetric with respect to zero

    :param value: the value which should be zero
    :param slope: the slope of the linear penalty to apply
    :return: the mark for the value, floored to 0
    """
    mark = 1 + slope * abs(value)
    return max(mark, 0)


def compute_quad_factor_bandwidth(bandwidth, linear_factor=0):
    """
    Computes the quadratic factor for a given bandwidth, so that the mark is zero at +- bandwidth * 0.5

    :param bandwidth: the required bandwidth for the mark factor
    :param linear_factor: optional, the linear factor
    :return: the quadratic factor which yields a function with the required bandwidth
    """
    return (- 1 - linear_factor * bandwidth * 0.5) / ((bandwidth * 0.5) ** 2)
